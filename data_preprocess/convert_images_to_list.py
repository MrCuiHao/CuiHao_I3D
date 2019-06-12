# coding:utf8
import os
import random

list_path = "/home/zoro/AI/action_recognition/I3D-Tensorflow/list/ucf_list/list"
flow_path = "/media/zoro/ZORO/I3D/data/UCF-101_TEST/flows"
video_num = 5  # 视频个数
rn_list = random.sample(range(1, video_num + 1), video_num)


def convert():
    if not os.path.exists(list_path):
        os.makedirs(list_path)
    train_list = open(list_path + "/train.list", "w")
    test_list = open(list_path + "/test.list", "w")
    count = -1
    rn_list_index = 0
    for class_name in os.listdir(flow_path):
        count = count + 1
        class_path = os.path.join(flow_path, class_name)
        for video_name in os.listdir(class_path):
            video_path = os.path.join(class_path, video_name)
            if rn_list[rn_list_index] > 1:
                train_list.write(video_path + " " + str(count) + "\n")
                rn_list_index = rn_list_index + 1
            else:
                test_list.write(video_path + " " + str(count) + "\n")
                rn_list_index = rn_list_index + 1


if __name__ == "__main__":
    convert()
