# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:40:58 2019

@author: Administrator
"""
"""
用代码打印出一个菱形
   *
  ***
 *****
*******
 *****
  ***
   *
"""
number = 4
for i in range(1,2*number):
    if i <= number:
        print(" "*abs(number-i)+"*"*(2*i-1))
    else:        
        print(" "*abs(number-i)+"*"*((2*i-1)-4*(i-number)))
