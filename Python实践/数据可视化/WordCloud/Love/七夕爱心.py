zhan# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 2019
@author: YangZ
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


text = "Love"   # 输入文字

# 从网上找了一个爱心的图片，获取图片轮廓
love_coloring = np.array(Image.open(path.join(d, "love1.jpg")))

# 设置词云参数
wc = WordCloud(
               background_color = "white",  #背景是白色
               repeat = True, # 单词可以重复               
               mask = love_coloring,  # 设置轮廓
               max_font_size = 100, # 最大字号
               random_state = 42,
               max_words = 1000, # 最多词个数
               colormap = "Oranges" # 选择色系
              )

# 从文本生成wordcloud
wc.generate(text)

# 根据图片，创建颜色（也可以用这个方式）
#image_colors = ImageColorGenerator(love_coloring)

# 绘制图片
plt.figure()    
plt.imshow(wc, interpolation="bilinear")
# plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

# 保存到文件
wc.to_file(path.join(d, "love.png"))
    
plt.show()