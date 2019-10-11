# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:43:32 2019

@author: Administrator
"""

"""
给定（可能有负数）整数序列A1, A2, A3..., An， 
求这个序列中子序列和的最大值。
（为方便起见，如果所有整数均为负数，则最大子序列和为0）。
例如：输入整数序列： -2, 11, 8, -4, -1, 16, 5, 0，
则输出答案为35，即从A2～A7。
"""
#number = input("整数序列：")
number = [1,2,3,-100,80]
#number = [-2, 11, 8, -4, -1, 16, 5, 0]
sum_n = []
for i in range(len(number)):
    sum_n.append(number[i])
    for j in range(i):
        sum_n.append(sum(number[j:i+1]))
print(max(sum_n))
        
    
 