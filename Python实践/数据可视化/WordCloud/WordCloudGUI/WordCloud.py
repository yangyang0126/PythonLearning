# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:02:04 2019

@author: Administrator
"""
import os
from os import path
# from matplotlib import pyplot as plt
import jieba
import easygui as g
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 用户设定初始值
def Para(values):
    msg  =  "你可以修改下面的默认参数" 
    title  =  "参数设置"
    fieldNames = [
                    "字体路径" ,  # fieldValues[0]
                    "显示词数",  # fieldValues[1]
                    "最大字号" ,  # fieldValues[2]
                    "背景色",  # fieldValues[3]
                    "轮廓宽度",  # fieldValues[4]
                    "轮廓颜色",  # fieldValues[5]
                    "轮廓参照",  # fieldValues[6]
                    "和图片顺色"     # fieldValues[7]                                 
                    ] 
    fieldValues  =  []  
    fieldValues  =  g.multenterbox (msg, title, fieldNames,values = values)
    return fieldValues

# 用户设定初始值-背景轮廓和颜色
def Para_mask(fieldValues):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask_image = path.join(d,'mask.jpg')
    if_mask = g.buttonbox("需要指定形状吗？\n默认是长方形\n你可以输入一张图片作为轮廓", image = mask_image,choices=("需要","不需要"))
    if if_mask == "需要":
        fieldValues[6] = g.fileopenbox(msg = '后缀为图片格式', title = '设置mask路径', default="*.png")
        #mask = np.array(Image.open(path_mask))
        color_image = path.join(d,'colored.png')
        if_color = g.buttonbox("需要和图片顺色吗？左边是不顺色，中间是顺色，右边是原图", image = color_image, choices=("需要","不需要"))
        if if_color == "需要":
            fieldValues[7] = 'True'
        else:
            fieldValues[7] = 'False'  
    else:
        fieldValues[6] = 'False'  
            
    return fieldValues

# 是否需要继续优化参数
def IfContinue(WC_continue, path_image, fieldValues):
    
    if WC_continue == "继续优化参数" :
        fieldValues = Para_mask(fieldValues)
        fieldValues = Para(fieldValues)
        if fieldValues[6] == 'False':
            wc =  SetWordCloud(fieldValues)  
            wc.generate(text)
            wc.to_file('image.png')  # 储存图像
            WC_continue = g.buttonbox(title="显示图像",msg='是否需要优化', image = path_image, choices=("继续优化参数","直接保存图像"))
            IfContinue(WC_continue, path_image, fieldValues)
        else:
            # 读取图片文件
            mask_coloring = np.array(Image.open(fieldValues[6]))
            wc =  SetWordCloudMask(mask_coloring, fieldValues) 
            wc.generate(text)
            if fieldValues[7] == 'False':
                wc.to_file('image.png')  # 储存图像
                # 调整图像显示大小
                im = Image.open(path_image)
                (x,y) = im.size #read image size
                y_s = 500 #define standard width
                x_s = int(x*y_s/y) #calc height based on standard width
                im = im.resize((x_s,y_s)) #resize image with high-quality
                im .save('image.png')
                WC_continue = g.buttonbox(title="显示图像",msg='是否需要优化', image = path_image, choices=("继续优化参数","直接保存图像"))
                wc.to_file('image.png')  # 储存图像
                IfContinue(WC_continue, path_image, fieldValues)
            else:
                # 根据图片，创建颜色
                image_colors = ImageColorGenerator(mask_coloring)
                # 储存图像
                wc.recolor(color_func = image_colors).to_file('image.png') 
            
                # 调整图像显示大小
                im = Image.open(path_image)
                (x,y) = im.size #read image size
                y_s = 500 #define standard width
                x_s = int(x*y_s/y) #calc height based on standard width
                im = im.resize((x_s,y_s)) #resize image with high-quality
                im .save('image.png')
                WC_continue = g.buttonbox(title = "显示图像",msg = '是否需要优化', image = path_image, choices=("继续优化参数","直接保存图像"))
                wc.recolor(color_func = image_colors).to_file('image.png') 
                IfContinue(WC_continue, path_image, fieldValues)

# 设置WordCloud参数，生成词云
def SetWordCloud(fieldValues):  
    wc = WordCloud(
            font_path = fieldValues[0],  #字体路径
            scale = 2,
            max_words = int(fieldValues[1]), #最多词个数
            max_font_size = int(fieldValues[2]),  #最大字号
            background_color = fieldValues[3],  #背景色
            contour_width = int(fieldValues[4]),  #设置轮廓宽度
            contour_color = fieldValues[5]  #设置轮廓颜色     
            )
    return wc

# 设置WordCloud参数，生成词云
def SetWordCloudMask(mask_coloring, fieldValues):   
    wc = WordCloud(
            font_path = fieldValues[0],  #字体路径
            scale = 2,
            max_words = int(fieldValues[1]), #最多词个数
            max_font_size = int(fieldValues[2]),  #最大字号
            background_color = fieldValues[3],  #背景色
            contour_width = int(fieldValues[4]),  #设置轮廓宽度
            contour_color = fieldValues[5],  #设置轮廓颜色
            mask = mask_coloring          
            )
    return wc

# 选择要输入的文件
path_text = g.fileopenbox(title = '请选择需要输入的内容（后缀为.txt）', default="*.txt")

# 显示文件
msg='文件内容如下：'
title='显示文件内容'
text = open(path_text, encoding='utf-8').read()
g.textbox(msg,title,text)

# 精确切割中文字符
text = ' '.join(jieba.cut(text, cut_all = False))

# 默认参数
fieldValues = [
               'C:/Windows/Fonts/simfang.ttf',
               100,
               100,
               'white',
               0,
               'steelblue',
               'False',
               'False'
             ]  
 
wc =  SetWordCloud(fieldValues)  

wc.generate(text)
wc.to_file('image.png')  # 储存图像

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本txt的路径（txt和代码在一个路径下面）
path_image = path.join(d,'image.png')
WC_continue = g.buttonbox(title="显示图像",msg='是否需要优化', image = path_image, choices=("继续优化参数","直接保存图像"))
IfContinue(WC_continue, path_image, fieldValues)

