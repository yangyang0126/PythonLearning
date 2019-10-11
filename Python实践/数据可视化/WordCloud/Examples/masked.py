#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# 获取文本txt的路径（txt和代码在一个路径下面）
text = open(path.join(d, 'BusinessEnglish.txt')).read()

# 读取mask的图像（图像和代码在一个路径下面）
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

# 设置不显示单词，比如said、in、on、is这种单词
stopwords = set(STOPWORDS)
stopwords.add("said")

# 设置词云参数
wc = WordCloud(background_color="white", 
               max_words=2000, 
               mask=alice_mask,
               stopwords=stopwords, 
               contour_width = 3,  #设置轮廓宽度
               contour_color = 'steelblue')  #设置轮廓颜色

# 从文本生成wordcloud
wc.generate(text)

# 保存到文件
wc.to_file(path.join(d, "alice.png"))

# 显示图片
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")

plt.figure()  #新建一个图片，把mask也显示出来
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")

plt.show()
