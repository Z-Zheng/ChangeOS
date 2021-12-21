
<h3 align="center">Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework:<br>from natural disasters to man-made disasters</h3>


<h5 align="right">by <a href="http://zhuozheng.top/">Zhuo Zheng</a>, <a href="http://rsidea.whu.edu.cn/">Yanfei Zhong</a>, <a href="https://junjue-wang.github.io/homepage/">Junjue Wang</a>, Ailong Ma and <a href="http://www.lmars.whu.edu.cn/prof_web/zhangliangpei/rs/index.html">Liangpei Zhang</a></h5>

[[`Paper`]](https://www.sciencedirect.com/science/article/pii/S0034425721003564) [[`BibTeX`](#Citation)]

<div align="center">
  <img src="https://raw.githubusercontent.com/Z-Zheng/images_repo/master/ChangeOS%400%2C25x.png"><br><br>
</div>


This is an official implementation of ChangeOS in our RSE 2021 paper [Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework: from natural disasters to man-made disasters](https://www.sciencedirect.com/science/article/pii/S0034425721003564).


---------------------

## Highlights

- Deep object-based semantic change detection framework (ChangeOS) is proposed.
- ChangeOS seamlessly integrates object-based image analysis and deep learning.
- City-scale building damage assessment can be achieved within one minute.
- A global-scale dataset is used to evaluate the effectiveness of ChangeOS.
- Two local-scale datasets are used to show its great generalization ability.



## Getting Started
### Installation

```bash
pip install changeos
```

#### Requirements:
- pytorch == 1.10.0
- python >=3.6
- skimage
- Pillow

### Usage

```python
# changeos has four APIs
# (e.g., 'list_available_models', 'from_name', 'visualize', 'demo_data')
import changeos


# constructing ChangeOS model
# support 'changeos_r18', 'changeos_r34', 'changeos_r50', 'changeos_r101'
model = changeos.from_name('changeos_r101') # take 'changeos_r101' as example

# load your data or our prepared demo data
# numpy array of shape [1024, 1024, 3], [1024, 1024, 3]
pre_disaster_image, post_disaster_image = changeos.demo_data()

# model inference
loc, dam = model(pre_disaster_image, post_disaster_image)

# put color map on raw prediction
loc, dam = changeos.visualize(loc, dam)

# visualize by matplotlib
import matplotlib.pyplot as plt
plt.subplot(121)
plt.imshow(loc)
plt.subplot(122)
plt.imshow(dam)
plt.show()

```



## <a name="Citation"></a>Citation
If you use ChangeOS in your research, please cite the following paper:
```text
@article{zheng2021building,
  title={Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework: from natural disasters to man-made disasters},
  author={Zheng, Zhuo and Zhong, Yanfei and Wang, Junjue and Ma, Ailong and Zhang, Liangpei},
  journal={Remote Sensing of Environment},
  volume={265},
  pages={112636},
  year={2021},
  publisher={Elsevier}
}
```