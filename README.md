
<h3 align="center">Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework:<br>from natural disasters to man-made disasters</h3>


<h5 align="right">by <a href="http://zhuozheng.top/">Zhuo Zheng</a>, <a href="http://rsidea.whu.edu.cn/">Yanfei Zhong</a>, <a href="https://junjue-wang.github.io/homepage/">Junjue Wang</a>, Ailong Ma and <a href="http://www.lmars.whu.edu.cn/prof_web/zhangliangpei/rs/index.html">Liangpei Zhang</a></h5>

[[`Paper`]](https://www.sciencedirect.com/science/article/pii/S0034425721003564) [[`BibTeX`](#Citation)]

<div align="center">
  <img src="https://raw.githubusercontent.com/Z-Zheng/images_repo/master/ChangeOS%400%2C25x.png"><br><br>
</div>


This is an official implementation of ChangeOS in our RSE 2021 paper [Building damage assessment for rapid disaster response with a deep object-based semantic change detection framework: from natural disasters to man-made disasters](#).


---------------------

## Highlights

- Deep object-based semantic change detection framework (ChangeOS) is proposed.
- ChangeOS seamlessly integrates object-based image analysis and deep learning.
- City-scale building damage assessment can be achieved within one minute.
- A global-scale dataset is used to evaluate the effectiveness of ChangeOS.
- Two local-scale datasets are used to show its great generalization ability.



## Getting Started
### Install EVER

```bash
pip install --upgrade git+https://github.com/Z-Zheng/ever.git
```

#### Requirements:
- pytorch >= 1.7.0
- python >=3.6

### TBD


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