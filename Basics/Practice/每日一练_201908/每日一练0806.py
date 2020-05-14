# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 09:41:53 2019

@author: Administrator
"""
# 参考答案
def solution(str1):
  y,m,d=map(int,str1.split("-"))
  D=0
  days=[31,0,31,30,31,30,31,31,30,31,30,31]
  if ((y%400==0)|((y%4==0)&(y%100!=0))):
    days[1]=29
  else:
    days[1]=28
  for i in range(m-1):
    D=D+days[i]
  return(D+d)
print(solution("2050-10-01"))