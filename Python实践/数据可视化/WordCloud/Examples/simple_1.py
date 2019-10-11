# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:08:51 2019

@author: YangYang
"""

import os
from os import path
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import easygui

easygui.msgbox("请选择需要输入的内容（后缀为.txt）")
path_text = easygui.fileopenbox(default="*.txt")

# 获取当前文件路径
#d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本txt的路径（txt和代码在一个路径下面）
#text = open(path.join(d,'path_text.txt')).read()

text = open(path_text).read()

# 设置词云参数
wc = WordCloud(
        scale=2,
        max_font_size=100,  #最大字号
        background_color='white'  #设置背景颜色
        )

wc.generate(text)  # 从文本生成wordcloud
# wc.generate_from_text(text)  #用这种表达方式也可以  

# 显示图像
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()

#wc.to_file('标签云效果图.png')  # 储存图像
#plt.savefig('标签云效果图.png',dpi=200)  #用这个可以指定像素
plt.show()