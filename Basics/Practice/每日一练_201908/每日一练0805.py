# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 09:44:35 2019

给定一个奇数，
然后判断最少几个 9 除于该数的结果为整数。

solution(13) ➞ 6
#999999/13=76923

solution(3) ➞ 1
#9/3=3

solution(7) ➞6
#999999/7=142857

"""
#  作业
def solution(num):
    i = 1
    while True:        
        number = []
        for n in range(i):
            number.append('9')
        number = int("".join(number))
        if number%num == 0:
            break
        else:
            i += 1
    return i   
print(solution(13))

# 参考答案
def solution(num):
  a=9
  i=1
  while a%num !=0:
    a=a*10+9
    i+=1
  return i
print(solution(3))