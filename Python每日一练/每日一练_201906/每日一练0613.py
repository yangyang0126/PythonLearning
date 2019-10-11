# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:46:53 2019

@author: Administrator
"""

"""
有一对兔子，从出生后第三个月起
每月都生出一对兔子
小兔子涨到第三个月后，每月又生一对兔子
假如兔子都不死，问每个月兔子总数为多少
"""
    
# 网上答案是这样的
a=1
b=1
print(a*2)
print(b*2)
for i in range(9):
    a=a+b
    print(a*2)
    b=a+b
    print(b*2)

