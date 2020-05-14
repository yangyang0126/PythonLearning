# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:30:16 2019

给定一个正整数数组，它的第 i 个元素是比特币第 i 天的价格。 
如果你最多只允许完成一笔交易（即买入和卖出一次），
设计一个算法来计算你所能获取的最大利润。
注意:不能在买入比特币前卖出。
"""
# 作业
def solution(lst):
    buy_min = min(lst[:-1])
    loc_min = lst.index(min(lst[:-1]))
    buy_max = max(lst[loc_min:])
    return (buy_max-buy_min)
print(solution([7,2,5,2,1,2,6,3]))
print(solution([600,482,520,500,803,585]))

# 参考答案
def solution(lst):
  sum=0
  while len(lst)!=1:
    a=lst.pop(0)
    b=max(lst)
    if b-a>sum:
      sum=b-a
  return sum
print(solution([600,482,520,500,803,585]))