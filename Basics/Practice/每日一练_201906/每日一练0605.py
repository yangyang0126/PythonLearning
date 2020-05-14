# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:08:07 2019

@author: Administrator
"""

"""
两个乒乓球队进行比赛，各出三人
甲队为a,b,c三人，乙队为x,y,z三人
已确定比赛名单
a说他不和x比
c说他不和x,z比
请找出三队赛手的名单
"""

team = ["x" , "y" , "z"] 
for a in team:
  for b in team: 
    for c in team:
      if a != b and a != c and b != c and a != "x" and c != "x" and c != "z":
          print("a的对手是{}，b的对手是{}，c的对手是{}".format(a , b , c))
   
