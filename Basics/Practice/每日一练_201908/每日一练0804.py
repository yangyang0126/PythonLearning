# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:02:21 2019

写一个函数，判断两条直线是否平行。

行由列表 [a，b，c] 表示，其对应于行 ax + by = c。
"""
# 作业
def solution(l1,l2):
    if l1[0]/l1[1] == l2[0]/l2[1]:
        return True
    else:
        return False

print(solution([1, 2, 3], [1, 2, 4]))

# 参考答案
def solution(l1, l2):
	a1, b1, a2, b2 = l1[0], l1[1], l2[0], l2[1]
	return (a1/b1) == (a2/b2)

print(solution([2, 4, 1], [4, 2, 1]))