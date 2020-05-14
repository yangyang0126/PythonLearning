# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:18:40 2020
@author: Yenny
"""

import os
from PIL import Image

# 原图片路径
path = "C:\\Users\\admin\\Desktop\\Bokeh"  

# 新建Resize这个文件夹，保存你调整尺寸后的图片
# 这个文件夹和你原来的图片文件夹在一个路径下
resizePath = path+'Resize'

try:
    os.mkdir(resizePath)  
except:
    pass


# 设置图片调整后的尺寸
# 每一张图调成一样的尺寸
sizeWeightEach = 512
sizeHeightEach = 512

# 设置拼图的行数和列数
numberColumns = 8  # 列数
numberRow = 4  # 行数

# 计算拼图的画布尺寸
sizeWeight = numberColumns*sizeWeightEach
sizeHeight = numberRow*sizeHeightEach

# 新建一个画布
newImage = Image.new('RGBA', (sizeWeight, sizeHeight)) 

# 获取全部文件名 
fileName = os.listdir(path)  


w = 8 # 设置边框宽度 
color = "green"
def AddBorder(w,color,image):  
    location = int(w/2)
    imageBorder = Image.new("RGB", (image.width + w, image.height + w), color)
    imageBorder.paste(image, (location, location)) 
    return imageBorder

count = 0 # 记录图片的顺序    
for i in range(1,numberColumns+1):
    for j in range(1,numberRow+1):        
        try:   
            name = fileName[count]
            image = Image.open(path+"\\"+name)
            image = AddBorder(w,color,image)     
            imageSize = image.resize((sizeWeightEach, sizeHeightEach),Image.ANTIALIAS)  # 调整图片尺寸
            imageSize.save(resizePath+"\\"+name)  # 保存调整后的图片（不需要的话，也可以不保存）
            newImage.paste(imageSize, ((i-1) * sizeWeightEach, (j-1) * sizeHeightEach))
            count += 1
        except:     
            name = fileName[count+1]
            image = Image.open(path+"\\"+name)
            image = AddBorder(w,color,image)     
            imageSize = image.resize((sizeWeightEach, sizeHeightEach),Image.ANTIALIAS)  # 调整图片尺寸
            imageSize.save(resizePath+"\\"+name)  # 保存调整后的图片（不需要的话，也可以不保存）
            newImage.paste(imageSize, ((i-1) * sizeWeightEach, (j-1) * sizeHeightEach))
            count += 2
            
newImage = AddBorder(w*3,color,newImage)
            
newImage.show()    
newImage.save(resizePath+"\\"+'PinJie.png')
    