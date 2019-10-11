# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:18:35 2019

@author: Administrator
"""

# 矩阵转置
import numpy as np
x= [[12,7,3],
    [4,5,6],
    [7,8,9]]
print(np.array(x).T)

# 另一种方式
print([[row[i] for row in x] for i in range(len(x[0]))])
