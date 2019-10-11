#!/usr/bin/env python
"""
Image-colored wordcloud
=======================

You can color a word-cloud by using an image-based coloring strategy
implemented in ImageColorGenerator. It uses the average color of the region
occupied by the word in a source image. You can combine this with masking -
pure-white will be interpreted as 'don't occupy' by the WordCloud object when
passed as mask.
If you want white as a legal color, you can just pass a different image to
"mask", but make sure the image shapes line up.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# 获取文本txt的路径（txt和代码在一个路径下面）
text = open(path.join(d, 'BusinessEnglish.txt')).read()

# 读取我要的图片文件
alice_coloring = np.array(Image.open(path.join(d, "alice_color.png")))

# 设置不显示的单词
stopwords = set(STOPWORDS)
stopwords.add("said")

# 设置词云参数
wc = WordCloud(background_color="white", 
               max_words=2000, 
               mask=alice_coloring,
               stopwords=stopwords, 
               max_font_size=40, 
               random_state=42)

# 从文本生成wordcloud
wc.generate(text)

# 根据图片，创建颜色
image_colors = ImageColorGenerator(alice_coloring)

# 把图片分成3份
fig, axes = plt.subplots(1, 3)

axes[0].imshow(wc, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()

# 单独显示图片    

# plt.figure()    
# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")

# plt.figure()    
# plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# plt.axis("off")

# plt.figure()    
# plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
# plt.axis("off")
    
plt.show()
