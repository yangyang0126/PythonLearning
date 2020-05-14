# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:06:48 2019

@author: YangYang

给定任何数字，我们可以通过添加该数字的数字平方和来创建新数字。 
例如，给定203，我们的新数字是4 + 0 + 9 = 13.
如果重复这个过程，将得到一系列数字：

203 -> 13 -> 10 -> 1 -> 1

有时，与203一样，序列最后等于1。这样的数字称为快乐数字。

并非所有数字都是快乐数字。 如果我们从11开始，序列将是：

11 -> 2 -> 4 -> 16 -> ...

此序列永远不会等于1，因此11称为不快乐数字。

给定正整数，您必须确定该数字是满意还是不满意。
"""
def add_square(n):
    return sum([int(i)**2 for i in str(n)])

def solution(n):
    temp = add_square(n)
    for i in range(1000):        
        if(temp) == 1:
            return True
        else:
            temp = add_square(temp)
    return False


print(solution(203))
print(solution(11))
print(solution(107))