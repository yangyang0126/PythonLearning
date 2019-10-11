# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:08:38 2019

@author: Administrator
"""

# 使用scatter() 绘制散点图并设置其样式
import matplotlib.pyplot as plt

x_value = list(range(1,10))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, c = 'red', edgecolor = 'none', s = 50)
# edgecolor: 数据点轮廓
# c:数据点颜色，默认是蓝色

# 颜色映射
plt.scatter(x_value, y_value, c = y_value, cmap = plt.cm.Blues, edgecolor = 'none', s = 50)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 10, 0, 100])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight') # 自动保存图表