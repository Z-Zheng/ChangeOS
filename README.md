
<h3 align="center">Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework:<br>from natural disasters to man-made disasters</h3>


<h5 align="right">by <a href="http://zhuozheng.top/">Zhuo Zheng</a>, <a href="http://rsidea.whu.edu.cn/">Yanfei Zhong</a>, <a href="https://junjue-wang.github.io/homepage/">Junjue Wang</a>, Ailong Ma and <a href="http://www.lmars.whu.edu.cn/prof_web/zhangliangpei/rs/index.html">Liangpei Zhang</a></h5>

[[`Paper (soon)`](#)] [[`BibTeX`](#Citation)]

<div align="center">
  <img src="https://raw.githubusercontent.com/Z-Zheng/images_repo/master/ChangeOS%400%2C25x.png"><br><br>
</div>


<p align="justify">
Sudden-onset natural and man-made disasters represent a threat to the safety of human life and property. Rapid and accurate building damage assessment using bitemporal high spatial resolution (HSR) remote sensing images can quickly and safely provide us with spatial distribution information and statistics of the damage degree to assist with humanitarian assistance and disaster response. For building damage assessment, strong feature representation and semantic consistency are the keys to obtaining a high accuracy. However, the conventional object-based image analysis (OBIA) framework using a patch-based convolutional neural network (CNN) can guarantee semantic consistency, but with weak feature representation, while the Siamese fully convolutional network approach has strong feature representation capabilities but is semantically inconsistent. In this paper, we propose a deep object-based semantic change detection framework, called ChangeOS, for building damage assessment. To seamlessly integrate OBIA and deep learning, we adopt a deep object localization network to generate accurate building objects, in place of the superpixel segmentation commonly used in the conventional OBIA framework. Furthermore, the deep object localization network and deep damage classification network are integrated into a unified semantic change detection network for end-to-end building damage assessment. This also provides deep object features that can supply an object prior to the deep damage classification network for more consistent semantic feature representation. Object-based post-processing is adopted to further guarantee the semantic consistency of each object. The experimental results obtained on a global scale dataset including 19 natural disaster events and two local scale datasets including the Beirut port explosion event and the Bata military barracks explosion event show that ChangeOS is superior to the currently published methods in speed and accuracy, and has a superior generalization ability for man-made disasters.
</p>

This is an official implementation of ChangeOS in our RSE 2021 paper [Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework: from natural disasters to man-made disasters](#).


---------------------

## Highlights

- Deep object-based semantic change detection framework (ChangeOS) is proposed.
- ChangeOS seamlessly integrates object-based image analysis and deep learning.
- City-scale building damage assessment can be achieved within one minute.
- A global-scale dataset is used to evaluate the effectiveness of ChangeOS.
- Two local-scale datasets are used to show its great generalization ability.


## <a name="Citation"></a>Citation
If you use ChangeOS in your research, please cite the following paper:
```text
@article{zheng2021buildingdamage,
  title={Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework: from natural disasters to man-made disasters},
  author={Zheng, Zhuo and Zhong, Yanfei and Wang, Junjue and Ma, Ailong and Zhang, Liangpei},
  journal={Remote Sensing of Environment},
  volume={},
  pages={},
  year={2021},
  publisher={Elsevier}
}
```



<!-- ## Getting Started
### Install EVER

```bash
pip install --upgrade git+https://github.com/Z-Zheng/ever.git
```

#### Requirements:
- pytorch >= 1.4.0
- python >=3.6 -->




