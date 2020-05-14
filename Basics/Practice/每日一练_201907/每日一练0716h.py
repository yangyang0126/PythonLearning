# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:08:40 2019

@author: Administrator
"""

# 注意：
# 1.在函数 solution 内补全你的代码
# 2.不要修改 solution 函数名，并且
# 要将结果 return 出来，否则你的代
# 码将无法通过测试
def solution(lst, el):
    location = []
    for i in range(len(lst)):
        if lst[i]== el:
            location.append(i)
    return location

print(solution(["a", "a", "b", "a", "b", "a"], "a"))
print(solution([1, 5, 5, 2, 7], 5))
print(solution([1, 5, 5, 2, 7], 8))