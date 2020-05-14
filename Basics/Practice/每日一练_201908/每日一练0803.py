# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:09:24 2019

 他从系统中调出一个字典，
 其中包含每单杯成本价格，单杯售价和卖出杯数。
 请你写一个函数，返回所得的总利润(四舍五入)。
 
 solution({
  "cost_price": 18.67,
  "sell_price": 25.00,
  "inventory": 1200
}) ➞ 7596

solution({
  "cost_price": 25.89,
  "sell_price": 33.00,
  "inventory": 100
}) ➞ 711

"""

# 作业
d={
  "cost_price": 18.67,
  "sell_price": 25.00,
  "inventory": 1200
}

def solution(dit):
  return round((dit["sell_price"]-dit["cost_price"])*dit["inventory"])

print(solution(d))


# 参考答案
d={
  "cost_price": 18.67,
  "sell_price": 25.00,
  "inventory": 1200}

def solution(dit):	
	a = dit["cost_price"]*dit["inventory"]
	b = dit["sell_price"]*dit["inventory"]
	return round(b-a)	

print(solution(d))