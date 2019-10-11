# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 08:41:20 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
import wordcloud  

# 设置词云参数
c = wordcloud.WordCloud(
               background_color = "white",  #背景是白色
               repeat = True, # 单词可以重复 
               max_font_size = 100, # 最大字号
               random_state = 42,
               max_words = 1000, # 最多词个数
               colormap = "gist_rainbow" # 选择色系
               )

# 从文本生成wordcloud
c.generate("python by wordcloud")

# 绘制图片
plt.figure()    
plt.imshow(c, interpolation="bilinear")
plt.axis("off")