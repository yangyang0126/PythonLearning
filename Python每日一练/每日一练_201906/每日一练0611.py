# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:26:36 2019

@author: Administrator
"""

"""
假设你要爬一个有n级台阶的梯子，每次可以走1步，也可以走2步。
请问，爬这个n级梯子，总共有几种方法
"""
n = 20
def step(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return step(n-1) + step(n-2)  
s = step(n)
print(s)