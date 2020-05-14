# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:47:44 2019

@author: Administrator
"""
# 作业
def solution(m,n):
    count = 0
    for i in range(m,n+1):
        if sum(list(range(1,i+1)))%3 == 0:
            count+=1
    return count
print(solution(5,15))

# 参考答案
def solution(m,n):
    nn=n//3*2+ (1 if n%3==2 else 0)
    mm=(m-1)//3*2+ (1 if (m-1)%3==2 else 0)
    return(nn-mm)
print(solution(5,15))