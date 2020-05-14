# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:50:05 2020

@author: zhaoy
"""

import requests  # 获取网页数据
import datetime
import xlwt
import pandas as pd



class Shanbey(): 
    def __init__(self, name, read, listen):
        self.Word = name
        self.Read = read
        self.Listen = listen
        
def SaveRecond(ID):
    # 准备表格
    workbook = xlwt.Workbook()  #定义workbook
    sheet = workbook.add_sheet('2020')  #添加sheet
    head = ['date', 'bdc','listen','read','time_bdc','time_listen','time_read']
    for h in range(len(head)):
        sheet.write(0, h, head[h])    #把表头写到Excel里面去
    ExcelRow = 1; #定义Excel表格的行数，从第二行开始写入，第一行已经写了表头
    
    # 读取数据
    try:    
        for Page in range(1,10):
            Web = "https://www.shanbay.com/api/v1/checkin/user/"+str(ID)+"/"+"?page="+str(Page)
            Res = requests.get(Web)
            DataEveryPage = Res.json()
            
            End = str(datetime.date(2020,1,1)).split(" ")[0]   
            
            for data in DataEveryPage['data']:
                if data['info']!='':
                    if data['checkin_date'] >= End:
                        sheet.write(ExcelRow, 0, data['checkin_date'])  
                        try:
                            sheet.write(ExcelRow, 1, data['stats']['bdc']['num_today'])
                            sheet.write(ExcelRow, 4, data['stats']['bdc']['used_time'])                   
                        except:
                            sheet.write(ExcelRow, 1, 0) 
                            
                        try:
                            sheet.write(ExcelRow, 2, data['stats']['listen']['num_today'])
                            sheet.write(ExcelRow, 5, data['stats']['listen']['used_time'])                   
                        except:
                            sheet.write(ExcelRow, 2, 0)  
                            sheet.write(ExcelRow, 5, 0)  
                            
                        try:
                            sheet.write(ExcelRow, 3, data['stats']['read']['num_today'])
                            sheet.write(ExcelRow, 6, data['stats']['read']['used_time'])                   
                        except:
                            sheet.write(ExcelRow, 3, 0)  
                            sheet.write(ExcelRow, 6, 0)       
                        ExcelRow += 1
                    else:
                        break
        workbook.save('Shanbey.xls')
        return True
    except:
        return False

def ReadRecond(ID):
    if SaveRecond(ID):
        df = pd.read_excel('Shanbey.xls')
        df['date'] = pd.to_datetime(df['date']) 
        df = df.set_index('date') # 将date设置为index   
        Record = Shanbey(df['bdc'].sum(),df['read'].sum(),df['listen'].sum())      
        return Record 
    else:
        return False

#ID = 16888030        
#Record = ReadRecond(ID)
#print(Record.Word)