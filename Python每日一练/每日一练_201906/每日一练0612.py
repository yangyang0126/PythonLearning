# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:06:59 2019

@author: Administrator
"""

"""
输入任意整数，找到从0到这个数中，
所有不能被3整除，也不含有3的数字
"""
n = input("请输入一个整数：")
n = [i for i in range(0,int(n)+1) if i%3 != 0]
[n.remove(i) for i in n for j in str(i) if j=="3"]
print(n)

