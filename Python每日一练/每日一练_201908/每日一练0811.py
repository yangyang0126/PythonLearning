# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:47:01 2019

@author: Administrator
"""

def solution(strs,n):
    s = []
    if len(strs)>=n:
        for i in range(len(strs)-n+1):
            s.append(strs[i:i+n])
        return (",".join(s))
    else:
        return ('-1')
            

print(solution('1234',5))
print(solution('12',2))
print(solution('123456789',6))