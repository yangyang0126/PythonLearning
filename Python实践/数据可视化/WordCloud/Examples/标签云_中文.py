# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:02:04 2019

@author: Administrator
"""

import os
from os import path
from wordcloud import WordCloud
from matplotlib import pyplot as plt

import jieba

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本txt
text = open(path.join(d,'商务英语.txt'),encoding='utf-8').read()
# 设置中文字体
font_path = 'C:\Windows\Fonts\simfang.ttf'  # 字体路径
# 精确切割中文字符
text = ' '.join(jieba.cut(text, cut_all = False))

# 生成词云
wc = WordCloud(
        font_path = font_path,  #字体路径
        scale=2,
        max_words = 100, #最多词个数
        max_font_size=100,  #最大字号
        background_color='white'  #背景色
        )
wc.generate(text)
# 显示图像
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
# 储存图像
#wc.to_file('标签云效果图.png')
#plt.savefig('标签云效果图.png',dpi=200)
plt.show()