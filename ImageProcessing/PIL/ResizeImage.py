# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:48:17 2020
@author: Yenny
"""

import os
from PIL import Image

path = "C:\\Users\\admin\\Desktop\\图片"  # 原图片路径
newPath  = "C:\\Users\\admin\\Desktop\\ResizeImage"  # 修改后的图片路径，你需要提前建好文件夹

# 设置图片调整后的尺寸
sizeWeight = 128
sizeHeight = 128

# 打开文件夹
fileName = os.listdir(path)  # 获取全部文件名 
for name in fileName:
    image = Image.open(path+"\\"+name)
    imageSize = image.resize((sizeWeight, sizeHeight),Image.ANTIALIAS)
    imageSize.save(newPath+"\\"+name)
