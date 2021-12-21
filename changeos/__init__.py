import os
import sys

import numpy as np
from skimage import measure
from skimage.io import imread
from torch.hub import download_url_to_file, get_dir
import torch
import torchvision.transforms.functional as F
from PIL import Image
from urllib.parse import urlparse

__all__ = ['from_name', 'list_available_models', 'visualize']
V = 0.2

AVAILABLE_MODELS = dict(
    changeos_r18=f'https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r18.pt',
    changeos_r34=f'https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r34.pt',
    changeos_r50=f'https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r50.pt',
    changeos_r101=f'https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/changeos_r101.pt',
)


class ChangeOS(object):
    def __init__(self, jit_model):
        self.model = jit_model
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model.to(self.device)

    def __call__(self, pre_disaster_image, post_disaster_image):
        image = np.concatenate([pre_disaster_image, post_disaster_image], axis=2)
        image = torch.from_numpy(image).permute(2, 0, 1).float()

        image = F.normalize(image,
                            mean=[123.675, 116.28, 103.53, 123.675, 116.28, 103.53],
                            std=[58.395, 57.12, 57.375, 58.395, 57.12, 57.375],
                            inplace=True)

        image = image.unsqueeze(0).to(self.device)
        loc, dam = self.model(image)

        loc, dam = object_based_infer(loc, dam)
        loc = loc.squeeze().astype(np.uint8)
        dam = dam.squeeze().astype(np.uint8)

        return loc, dam


def object_based_infer(pre_logit, post_logit):
    loc = (pre_logit > 0.).cpu().squeeze(1).numpy()
    dam = post_logit.argmax(dim=1).cpu().squeeze(1).numpy()

    refined_dam = np.zeros_like(dam)
    for i, (single_loc, single_dam) in enumerate(zip(loc, dam)):
        refined_dam[i, :, :] = _object_vote(single_loc, single_dam)

    return loc, refined_dam


def _object_vote(loc, dam):
    damage_cls_list = [1, 2, 3, 4]
    local_mask = loc
    labeled_local, nums = measure.label(local_mask, connectivity=2, background=0, return_num=True)
    region_idlist = np.unique(labeled_local)
    if len(region_idlist) > 1:
        dam_mask = dam
        new_dam = local_mask.copy()
        for region_id in region_idlist:
            if all(local_mask[local_mask == region_id]) == 0:
                continue
            region_dam_count = [int(np.sum(dam_mask[labeled_local == region_id] == dam_cls_i)) * cls_weight \
                                for dam_cls_i, cls_weight in zip(damage_cls_list, [8., 38., 25., 11.])]
            dam_index = np.argmax(region_dam_count) + 1
            new_dam = np.where(labeled_local == region_id, dam_index, new_dam)
    else:
        new_dam = local_mask.copy()
    return new_dam


def _download_model(name):
    assert name in list_available_models(), f'{name} is unsupported.'
    url = AVAILABLE_MODELS[name]
    hub_dir = get_dir()
    model_dir = os.path.join(hub_dir, 'checkpoints')
    parts = urlparse(url)
    filename = os.path.basename(parts.path)
    cached_file = os.path.join(model_dir, filename)
    if not os.path.exists(cached_file):
        sys.stderr.write('Downloading: "{}" to {}\n'.format(url, cached_file))
        os.makedirs(model_dir, exist_ok=True)
        download_url_to_file(url, cached_file)

    model = torch.jit.load(cached_file)
    return model


def list_available_models():
    return list(AVAILABLE_MODELS.keys())


def from_name(name):
    model = _download_model(name)
    model.eval()
    model = ChangeOS(model)
    return model


def visualize(loc, dam):
    loc = Image.fromarray(loc)
    loc.putpalette([0, 0, 0,
                    255, 255, 255])
    loc = loc.convert('RGB')
    loc = np.asarray(loc)

    dam = Image.fromarray(dam)
    dam.putpalette([0, 0, 0,
                    255, 255, 255,
                    0, 255, 0,
                    248, 179, 101,
                    255, 0, 0])
    dam = dam.convert('RGB')
    dam = np.asarray(dam)

    return loc, dam


def demo_data():
    pre = imread(f'https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/socal-fire_00000667_pre_disaster.png')
    post = imread(f'https://github.com/Z-Zheng/ChangeOS/releases/download/v{V}/socal-fire_00000667_post_disaster.png')
    return pre, post
