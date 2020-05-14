# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:39:36 2019

@author: Administrator
"""
"""
摄氏度和华氏度的转变
请输入温度：110C
转换温度为：230.0F
"""

data = input('请输入温度：')
if data[-1] == 'C':
    print('转换温度为：'+str(9*float(str(data[:-1]))/5+32)+'F')
else:
    print('转换温度为：'+str((float(str(data[:-1]))-32)*5/9)+'C')
    

