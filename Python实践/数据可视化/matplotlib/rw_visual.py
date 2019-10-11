# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:39:08 2019

@author: Administrator
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
                cmap=plt.cm.Blues, edgecolor='none', s=3)
    
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    
    keep_running = input("Make anoter walk? (y/n): ")
    if keep_running == 'n':
        break