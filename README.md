# 1、正则化技术

数据增强、L2、L1正则以及Dropout，[Drop Connect](https://nickcdryan.com/2017/06/13/dropconnect-implementation-in-python-and-tensorflow/)，Early stopping（避免过度训练）。

### 数据增强
[Here](https://medium.com/ymedialabs-innovation/data-augmentation-techniques-in-cnn-using-tensorflow-371ae43d5be9) <br>

数据增强库[Augmentor](https://augmentor.readthedocs.io/en/master/index.html)和[imgaug](https://imgaug.readthedocs.io/en/latest/index.html) , [介绍](https://www.cnblogs.com/vincentcheng/p/9186540.html)

# 2、优化器
[关于优化器的介绍](https://www.jianshu.com/p/e6e8aa3169ca)

sgd 以及 Momentum 更加适合小样本数据集的最优化。


# 3、怼网络
[S-NN: Stacked Neural Networks](https://arxiv.org/pdf/1605.08512.pdf)


# 4、其余trick
构建[高分辨率model](https://arxiv.org/ftp/arxiv/papers/1312/1312.5402.pdf)

# 5 Label数据不均衡

方式：
* 对损失函数加惩罚项，weights平衡。
* label多的数据欠采样，label少的过采样。
* 采用F1等指标均衡准确和召回。
