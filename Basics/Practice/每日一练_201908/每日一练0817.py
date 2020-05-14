# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 09:33:44 2019

创建一个对列表执行奇偶变换n次的函数。
每个奇偶变换：
每个奇数整数加2（+2）。
每个偶数整数减2（-2）。
"""

def solution(lst, n):
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            lst[i] = lst[i]-2*n
        else:
            lst[i] = lst[i]+2*n
    return lst
print(solution([3, 4, 9], 3))