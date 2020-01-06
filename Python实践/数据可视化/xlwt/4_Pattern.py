# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:03:47 2020

@author: admin
"""

import xlwt

# 定义保存Excel的位置
workbook = xlwt.Workbook()  #定义workbook
sheet = workbook.add_sheet('colour')  #添加sheet

style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式 style

# 设置居中
al = xlwt.Alignment()
al.horz = 0x02      # 设置水平居中
al.vert = 0x01      # 设置垂直居中

# 为样式设置边框
borders = xlwt.Borders() # Create Borders
borders.left = xlwt.Borders.THIN 
# DASHED虚线
# NO_LINE没有
# THIN实线
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left_colour = 1 # 白色边框
borders.right_colour = 1
borders.top_colour = 1
borders.bottom_colour = 1

# 为样式创建字体
font = xlwt.Font()  
font.name = 'Calibri' # 设置字体
font.colour_index = 1 # 设置字体颜色
font.height = 400 # 字体大小

# 定义格式
style.font = font
style.borders = borders 
style.alignment = al
    
# 控制行的位置
column = 0;
row = 0
# 写入数据
for i in range(72):
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = i  # 给背景颜色赋值    
    style.pattern = pattern  # 把背景颜色加到表格样式里去
    sheet.write(row, column, i, style) 
    column += 1
    if column > 8:
        column = 0
        row += 1
    
workbook.save('xlwt.xls')
