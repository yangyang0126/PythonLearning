# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:48:51 2019

@author: Administrator
"""

"""
有一分数序列：
2/1,3/2,5/3,8/5,13/8,21/13...
求出这个数列的前20项之和
"""

i = 2
j = 1
number = []
for n in range(1,21):
    number.append(i/j)
    i,j = j+i,i  
print(sum(number))
    
    