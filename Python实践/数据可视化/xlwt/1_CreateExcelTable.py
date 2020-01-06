# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:06:05 2020

@author: Yenny

如果你没有安装xlwt

请先 'pip install xlw' 安装库
"""

# 导入xlwt库
import xlwt

# 定义workbook
workbook = xlwt.Workbook() 

# 添加sheet，这个sheet的名字叫'Style'
sheet = workbook.add_sheet('Style')  

# 写入数据
row = 0 # 行
column = 0 # 列
for i in range(72):    
    sheet.write(row, column, i) # 写入数据，第row行，第column列，具体内容是i
    column += 1
    if column > 8:
        column = 0
        row += 1
        
# 定义保存Excel的位置
workbook.save('CreatExcelTable.xls')