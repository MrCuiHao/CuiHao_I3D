**一、引言**

  整个代码在UCF101数据集上微调I3D模型，包括训练阶段和测试阶段。
I3D文章:《Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset》
关于I3D的模型和细节请参考kinetics-i3d

**二、环境条件**
**软件**  
**硬件**
**、数据预处理**

**、数据预处理**

**、数据预处理**

**、数据预处理**

1、#data_preprocess/denseflow.py
把视频文件处理成RGB和光流数据,RGB就是从视频中一帧帧抽取的图片，光流是使用光流算法TVL1计算的结果，如图所示:

2、#data_preprocess/convert_images_to_list.py
这是把抽取好的RGB和光流结果转换成训练验证、测试列表..

3、后续会把I3D的训练步骤补充完整，敬请期待

4、test test
