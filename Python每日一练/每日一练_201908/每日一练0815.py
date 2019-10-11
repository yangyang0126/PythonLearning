# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:34:04 2019

小贝经常和闻闻一起吃午饭。

小贝比较重口，喜欢吃辣的饭菜，但闻闻一点辣也吃不了。
 于是，小贝经常一个人吃完了所有辣的菜品，同时还吃掉一半不辣的菜。
 今天，小贝摸着圆圆的肚子，终于良心发现，
 决定以后和闻闻分摊不辣的菜品，辣的菜自己支付。

小贝给你两个有序列表，一个将菜肴分为辛辣和非辣，
另一个列出它们的价格，请你写一个函数输出一个列表，
其中第一个元素是小贝支付金额，第二个元素是闻闻支付金额。
"""
# 作业
def solution(spicy, cost):
    cost_xiaobei = 0
    cost_wenwen = 0
    for i in range(len(spicy)):
        if spicy[i] == 'N':
            cost_xiaobei = cost_xiaobei+cost[i]/2
            cost_wenwen = cost_wenwen+cost[i]/2
        else:
            cost_xiaobei = cost_xiaobei+cost[i]            
    return [cost_xiaobei,cost_wenwen]

print(solution(["N", "N"], [10, 10]))
print(solution(["N", "S", "N"], [10, 10, 20]))

# 参考答案
def solution(spicy, cost):
	s = sum(y for (x,y) in zip(spicy,cost) if x=='S')
	n = (sum(cost)-s)
	return [n/2+s,n/2]

print(solution(["N", "N"], [10, 10]))