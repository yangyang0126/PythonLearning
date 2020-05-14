# -*- coding: utf-8 -*-
"""
Created on Fri May 17 2019

@author: YangYang
"""

'''
请确保你在运行这个代码的时候，已经安装了pdfplumber库
如果没有安装，请在[附件-命令提示符]下输入：
pip install pdfplumber
'''

import pdfplumber
import xlwt

# 定义保存Excel的位置
workbook = xlwt.Workbook()  #定义workbook
sheet = workbook.add_sheet('Sheet1')  #添加sheet
i = 0 # Excel起始位置

path = input("请输入PDF文件位置：")    
#path = "aaaaaa.PDF"  # 导入PDF路径
pdf = pdfplumber.open(path)
print('\n')
print('开始读取数据')
print('\n')
for page in pdf.pages:
    # 获取当前页面的全部文本信息，包括表格中的文字
    # print(page.extract_text())                     
    for table in page.extract_tables():
        # print(table)
        for row in table:            
            print(row)
            for j in range(len(row)):
                sheet.write(i, j, row[j])
            i += 1
        print('---------- 分割线 ----------')

pdf.close()

# 保存Excel表
workbook.save('C:/Users/Administrator/Desktop/PDFresult.xls')
print('\n')
print('写入excel成功')
print('保存位置：')
print('C:/Users/Administrator/Desktop/PDFresult.xls')
print('\n')
input('PDF取读完毕，按任意键退出')