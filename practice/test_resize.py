#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: Nasa
# Created: 2018-10-28 21:25 CST

import os
# 安装正确后cv2才可以被导入，否则将出现ImportError类错误
import cv2
file_list = [i for i in os.listdir("imgs") if i.endswith("JPG")] # 遍历得到文件夹下的图片得到列表
src_list = [os.path.join("imgs", i) for i in file_list] # 得到正确路径
read_list = [cv2.imread(i) for i in src_list] # 将图片读入内存
dest_list = [os.path.join("imgs_out", i) for i in file_list] #输出文件列表
print src_list

for i, v in enumerate(read_list):  # enumerate 生成数组index与值对,:后需要缩进
    print type(v)
    tmp = cv2.resize(v, (48,48)) # 将图片压缩成48*48
    cv2.imwrite(dest_list[i], tmp) #将压缩结果存imgs_out文件夹

