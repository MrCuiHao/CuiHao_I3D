**一、数据预处理**

1、#data_preprocess/denseflow.py
把视频文件处理成RGB和光流数据,RGB就是从视频中一帧帧抽取的图片，光流是使用光流算法TVL1计算的结果，如图所示:

2、#data_preprocess/convert_images_to_list.py
这是把抽取好的RGB和光流结果转换成训练验证、测试列表..