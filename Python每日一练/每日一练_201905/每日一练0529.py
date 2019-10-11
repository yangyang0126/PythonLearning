# -*- coding: utf-8 -*-
"""
Created on Wed May 29 2019

@author: YangYang
"""

"""
有四个数字：5，6，7，8
能组成多少不相同的，且不重复的三位数？
"""


# 第一种方法
"""
python内置函数-排列组合函数:
product 笛卡尔积（有放回抽样排列）
permutations 排列（不放回抽样排列）
combinations 组合,没有重复（不放回抽样组合）
combinations_with_replacement 组合,有重复（有放回抽样组合）
"""
import itertools
data = [5,6,7,8]
for i in itertools.permutations (data, 3):
    print(i[0]*100+i[1]*10+i[2])
    
# 第二种方法
for i in range(5,9):
    for j in range(5,9):
        for k in range(5,9):
            if i!=j and j!=k and i!=k:
                print(i*100+j*10+k)
    
    
    
    
    