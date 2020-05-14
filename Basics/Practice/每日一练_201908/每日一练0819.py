# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:57:06 2019

@author: Administrator
"""

def solution(lst):
    lst_new = []
    for i in range(len(lst)-1):  
        if lst[i] > max(lst[i+1:]):            
            lst_new.append(lst[i])     
    lst_new.append(lst[-1])
    return lst_new

print(solution([3, 13, 11, 2, 1, 9, 5]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([5, 9, 7, 8]))