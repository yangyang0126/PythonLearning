# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 2019

@author: YangYang
"""

"""
鸡兔同笼，头35，脚94.
问鸡和兔各有几只？
"""
head = 35
foot = 94

#  假设鸡是i，兔子是j
for i in range(head): 
    j = head - i
    if (i*2 + j*4) == foot:
        print (i,j)