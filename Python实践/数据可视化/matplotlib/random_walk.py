# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:58:37 2019

@author: Administrator
"""

# 随机漫步
from random import choice

# 初始化随机漫步的属性
class RandomWalk():
    def __init__(self, num_points=5000):
        
        self.num_points = num_points
        
        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    # 计算随机漫步包含的所有点        
    def fill_walk(self):
    
        # 不断漫步，直到列表达到指定的长度
         while len(self.x_values) < self.num_points:
         
             # 决定前进方向以及沿这个方向前进的距离
             x_direction = choice([1, -1])  # 向左走-1，向右走1
             x_distance = choice([0, 1, 2, 3, 4])
             x_step = x_direction * x_distance # 正数向右移动，负数向左移动
         
             y_direction = choice([1, -1])
             y_distance = choice([0, 1, 2, 3, 4])
             y_step = y_direction * y_distance # 正数向上移动，负数向下移动
         
             # 拒绝原地踏步
             if x_step == 0 and y_step == 0:
                 continue
         
             # 计算下一个点的x值和y值
             next_x = self.x_values[-1] + x_step
             next_y = self.y_values[-1] + y_step
         
             self.x_values.append(next_x)
             self.y_values.append(next_y)
         
         
         
         
         
    
    