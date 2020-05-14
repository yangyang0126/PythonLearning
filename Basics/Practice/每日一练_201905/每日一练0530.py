# -*- coding: utf-8 -*-
"""
Created on Thu May 30 2019

@author: YangYang
"""

"""
任意输入n个整数
把这n个数从大到小输出
"""
def CalMax(data):
    #data = data.split(" ")
    result = []
    for i in range(len(data)):
        x = max(data) 
        result.append(x)   
        data.remove(x)         
    print(result)
    
data = [1,3,12,4]
CalMax(data)

# 如果需要从小到大输出的话
# 把max改成min

# 另一个方法,直接用自带函数
def CalMax(data):    
    print(sorted(data))    
data = [1,3,12,4]
CalMax(data)