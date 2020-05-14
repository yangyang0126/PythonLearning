# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:00:25 2019

@author: Administrator
"""
# 作业
def Ori(direction,RL):    
    if direction == 'N':
        dirL = 'W'
        dirR = 'E'
    if direction == 'E':
        dirL = 'N'
        dirR = 'S'
    if direction == 'S':
        dirL = 'E'
        dirR = 'W'
    if direction == 'W':
        dirL = 'S'
        dirR = 'N'
    if RL == 'l':
        return dirL
    else:
        return dirR    
def solution(n,m):
    direction = 'N'
    for i in m:
        direction = Ori(direction,i)
    return direction   
print(solution(3,"lrr"))
print(solution(6,"rrrrlr"))
print(solution(5,"rlrll"))

# 参考答案
def solution(n,m):
  dict1={'1':'E','2':'S','3':'W','0':'N'}
  init=0
  for i in range(int(n)):
    if m[i]=='l':
      init-=1
    else:
      init+=1
  return(dict1[str(init%4)])

print(solution(6,"rrrrlr"))