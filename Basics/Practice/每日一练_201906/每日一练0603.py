# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 2019

@author: YangYang
"""
"""
打印出所有的水仙花数
水仙花数：一个3位数
各位数字的立方和等于该数字本身
例如153=1^3+5^3+3^3
"""
for i in range(100,1000):
    j = str(i)
    if (int(j[0])**3+int(j[1])**3+int(j[2])**3) == int(j):
        print(i)
