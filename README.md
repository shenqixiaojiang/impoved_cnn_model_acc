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

## 6 [神学调参](https://www.zhihu.com/question/41631631/answer/94935518)
* dropout：分类问题用dropout ，只需要最后一层softmax前用基本就可以了，能够防止过拟合，可能对accuracy提高不大，但是dropout前面的那层如果是之后要使用的feature的话，性能会大大提升。
* 正则化：一轮加正则，一轮不加正则，反复进行。
* 优化器：据说adadelta一般在分类问题上效果比较好，adam在生成问题上效果比较好。在小数据上,sgd收敛速度会慢一些，但是最终结果一般都比较好。
* 学习率：随着网络训练的进行，学习率要逐渐降下来，在学习率下降的一瞬间，网络会有个巨大的性能提升，同样的fine-tuning也要根据模型的性能设置合适的学习率，比如一个训练的已经非常好的模型你上来就1e-3的学习率，那之前就白训练了，就是说网络性能越好，学习率要越小。
* 特征拼接：不同尺寸的feature maps的concat，只用一层的feature map一把梭可能不如concat好。

## 7 海康威视(https://zhuanlan.zhihu.com/p/23249000)
* 在训练的最后几个epoch，移除数据增强，然后跟传统一样测试。
* 如果训练的时候一直使用尺度和长宽比增强数据增强，在测试的时候也同样做这个变化，随机取32个crop来测试。
* 多尺度的训练，多尺度的测试
* 使用训练过程的中间结果，加入做测试，可以一定程度上降低过拟合(多个模型求平均)

