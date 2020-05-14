# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:03:05 2020

@author: admin
"""

import requests  # 获取网页数据
from bs4 import BeautifulSoup  # 解析网页数据

# 从 openpyxl 引入 Workbook（工作簿）类
from openpyxl import Workbook


# 获取豆瓣网址并解析数据
def get_douban_books(url,num):
    res = requests.get(url)  # requests发起请求，静态网页用get
    soup = BeautifulSoup(res.text, 'html.parser')
    
    m = n = j = num
    
    items_title = soup.find_all("div", class_="pl2")    
    for i in items_title:        
        tag = i.find("a")        
        # 去掉空格和换行符
        name = ''.join(tag.text.split())
        link = tag["href"]
        title_markdown = "[{}]({})".format(name,link)
        sheet.write(m, 0, title_markdown)
        m += 1
        
    items_author = soup.find_all("p", class_="pl") 
    for i in items_author:              
        author_markdown = i.text
        sheet.write(n, 1, author_markdown)
        n += 1
        
    items_image = soup.find_all("a", class_="nbg")   
    for i in items_image:        
        tag = i.find("img")
        link = tag["src"]
        image_markdown = "![]({})".format(link)
        sheet.write(j, 2, image_markdown)
        j += 1
        

        

get_douban_books('https://book.douban.com/top250?start=1',1)




# 通过 Workbook 类实例化一个工作簿
wb = Workbook()

# 选择默认的工作表
sheet = wb.active
# 给工作表重命名
sheet.title = '8月考勤统计表'
# 写入多行数据
for row in data:
  sheet.append(row)
  
# 保存 Excel 文件
wb.save('考勤统计.xlsx')