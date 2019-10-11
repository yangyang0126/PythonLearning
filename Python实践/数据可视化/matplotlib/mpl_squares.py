# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:49:09 2019

@author: Administrator
"""
# 绘制简单的折线图
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]  # 横坐标
squares = [1, 4, 9, 16, 25]  # 纵坐标
plt.plot(input_values, squares, linewidth = 5)
# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

plt.show()