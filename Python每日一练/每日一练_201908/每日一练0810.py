# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:10:00 2019

@author: Administrator
"""

def solution(lst,limit):
  lst.sort()
  anw=0
  while lst:
    for j in lst[:0:-1]:
      if j+lst[0]<=limit:
        lst.remove(j)
        lst=lst[1:]
        anw+=1
        break
    else:
      return anw+len(lst)  
  
print(solution([110, 120, 150, 170, 200, 220],300))