# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019

@author: YangYang
"""

"""
在2000-3200中，
找到所有可以被7整除，
但不是5的倍数的整数
用range函数
"""
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)