# 读入分类的标签txt文件
#label_file = open("Users/86181/Desktop/VOC2028/ImageSets/Main/val.txt", 'r')
# 原始文件的根目录
#input_path =  "Users/86181/Desktop/yolov8/dataset/anquanmao/VOCdevkit/JPEGImages"
# 保存文件的根目录
#output_path = "Users/86181/Desktop/yolov8/dataset/anquanmao/images/val"
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:10:11 2020

@author: zqq
"""

import os 
import shutil

# 读取图片的路径
read_path = "/Users/86181/Desktop/yolov8/dataset/anquanmao/VOCdevkit/txt"
# 存放图片的路径
save_path = "/Users/86181/Desktop/yolov8/dataset/anquanmao/labels/test"
if not os.path.exists(save_path):
    os.mkdir(save_path)
fileType = '.jpg'
num = 0
# 读取并遍历读取txt中的每行
with open('/Users/86181/Desktop/VOC2028/ImageSets/Main/test.txt','r') as f:
    for name in f:
        fileName = name.strip() # 去除末尾的换行
        #print(fileName)
        #print(type(fileName)) # 查看文件类型
        
        # 读取并遍历文件夹中的图片
        for file in os.listdir(read_path):
            #print(file)
            #print(type(file))      
    
            if fileName+fileType == file:
                num+=1
                shutil.copy(os.path.join(read_path,fileName+fileType),save_path)
                print("%s Copy successfully"%(fileName+fileType))
    print("Copy complete!")
    print("Total pictures copied:",num)
                
### 测试
# shutil.copy('img_res/000001.jpg',save_path)
# fileName = '000001'
# shutil.copy(os.path.join(read_path,fileName+fileType),save_path)

