# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 08:43:15 2019

@author: Administrator
"""
# 作业
def solution(s, first, second):
    loc_second = s.index(second)
    s = s[::-1]
    loc_first = len(s)-s.index(first)+1    
    return loc_first<loc_second    

print(solution("a rabbit jumps joyfully", "a", "j"))
print(solution("knaves knew about waterfalls", "k", "w"))
print(solution("happy birthday", "a", "y"))
print(solution("precarious kangaroos", "k", "a"))

# 参考答案
def solution(s, first, second):
	fInd = max([i for i in range(len(s)) if s[i] == first])
	sInd = min([i for i in range(len(s)) if s[i] == second])
	return fInd < sInd

print(solution("a rabbit jumps joyfully", "a", "j"))