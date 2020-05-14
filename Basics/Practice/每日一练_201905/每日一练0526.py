# -*- coding: utf-8 -*-
"""
Created on Wed May 29 2019

@author: YangYang
"""

"""
编写函数，去除一个列表中不重复的元素，同时保持其顺序
例：
输入为 [3, 1, 2, 2, 3, 4, 3]
输出为 [3, 2, 2, 3, 3]
"""
def DelNumber(data):
    for i in data:
        if data.count(i) == 1:
            data.remove(i)
    print(data)

data = [3, 1, 2, 2, 3, 4, 3]
DelNumber(data)