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

# 添加sheet，这个sheet的名字叫'Font'
sheet = workbook.add_sheet('Font')  

# 为样式创建字体
def SetStyleFont(name,color,height,bold,italic,underline,struck_out):
    style = xlwt.XFStyle()  
    font = xlwt.Font()  
    font.name = name  # 设置字体    
    font.colour_index = color # 设置字体颜色
    font.height = height # 字体大小    
    font.bold = bold # 是否为粗体    
    font.italic = italic # 字体是否斜体    
    font.underline = underline # 是否有下划线    
    font.struck_out = struck_out # 字体中是否有横线
    style.font = font
    return style

# 写入数据
row = 0 # 行
column = 0 # 列
for i in range(72): 
    if i < 36:        
        sheet.write(row, column, i, SetStyleFont('Times New Roman',i,400,True,True,False,True)) 
    else:
        sheet.write(row, column, i, SetStyleFont('Times New Roman',i,400,False,False,False,True)) 
    column += 1
    if column > 8:
        column = 0
        row += 1
        
# 定义保存Excel的位置
workbook.save('Font.xls')