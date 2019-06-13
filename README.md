**一、引言**

  整个代码在UCF101数据集上微调I3D模型，包括训练阶段和测试阶段。
I3D文章:《Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset》
关于I3D的模型和细节请参考kinetics-i3d

**二、环境条件**

  **软件**
  
    Ubuntu 16.04.3 LTS
    Python 2.7
    CUDA8
    CuDNN v6
    Tensorflow 1.4.1
    Sonnet

  **硬件**
  
    GeForce GTX 1080 Ti
    
**三、数据预处理**

1、#data_preprocess/denseflow.py
把视频文件处理成RGB和光流数据,RGB就是从视频中一帧帧抽取的图片，光流是使用光流算法TVL1计算的结果，如图所示:

2、#data_preprocess/convert_images_to_list.py
这是把抽取好的RGB和光流结果转换成训练验证、测试列表..

3、后续会把RGB和光流的生成步骤补充完整，这里你们可以使用我总结的生成训练验证集、测试集的工具，如果你们有更好的方法
可以联系我，代码也可以提交给我，敬请期待。


**四、如何运行**

1.克隆下面的仓库

    git clone git@github.com:MrCuiHao/CuiHao_I3D.git

2.下载在kinetics数据集上预训练的I3D模型

    为了在UCF101数据集上微调I3D网络，必须要下载在kinetics数据集上预训练的I3D模型，此模型由DeepMind提供，
    先从github下载仓库kinetics-i3d，然后把仓库里的文件夹data/checkpoints放入我们CuiHao_I3D仓库的子目录data里。
    
        git clone https://github.com/deepmind/kinetics-i3d
        cp -r kinetics-i3d/data/checkpoints CuiHao_I3D/data
3.创建列表文件

    使用data/ucf101/子目录里的列表文件，从而使得代码能找到保存在磁盘上的RGB图片和光流数据。必须要采用列表文件，以确保列表文
    件包含数据对应的路径是正确的。具体来说，对于RGB数据，必须更新data/ucf101/rgb.txt。在这个文件的每一个行应该用一下格式：
    
        dir_name_of_imgs_of_a_video /path/to/img_dir num_imgs label
        视频图片所在目录名（视频名--去掉.avi .mp4这种格式名后的名字）视频图片目录对应的绝对路径 图片的数目 视频对应的类别

**、数据预处理**

**、数据预处理**


