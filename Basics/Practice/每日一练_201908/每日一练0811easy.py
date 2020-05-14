# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:09:27 2019

@author: Administrator
"""

def solution(n):
    result = lambda n: n if n < 2 else 2 * solution(n - 1)
    return result(n)
print(solution(5))