# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:03:41 2020
@author: Yenny
"""

import calendar 
import tkinter as tk
root = tk.Tk()

def LabelCal(Year, Month):
    # 首行放置“年、月”的位置
    label = tk.Label(root,text=str(Year)+"年")
    label.grid(row=0,column=2)
    label = tk.Label(root,text=str(Month)+"月")
    label.grid(row=0,column=4)
    # labels列表：放置“星期”的标题
    labels = [['Mon','Tue','Wed','Thu','Fri','Sat','Sun']]
    # 用calendar库计算日历
    MonthCal = calendar.monthcalendar(Year, Month)  
    # 先把界面清空
    for r in range(7):
        for c in range(7):            
            label = tk.Label(root,
                          width =5,
                          padx=5,
                          pady=5,
                          text=' ')        
            label.grid(row=r+1,column=c)
    # 把日历加到labels列表中     
    for i in range(len(MonthCal)):
        labels.append(MonthCal[i])
    # 放置日历
    for r in range(len(MonthCal)+1):
        for c in range(7):
            if labels[r][c] == 0:
                labels[r][c] = ' '
            label = tk.Label(root,
                          width =5,
                          padx=5,
                          pady=5,
                          text=str(labels[r][c]))        
            label.grid(row=r+1,column=c) # 网格布局
        
# button：Enter
def ButtonPrevious():
    global Year, Month
    Month = Month-1
    if Month<1:
        Month = Month+12
        Year = Year-1
    LabelCal(Year, Month)

# button：Clear
def ButtonNext():
    global Year, Month
    Month = Month+1
    if Month>12:
        Month = Month-12
        Year = Year+1 
    LabelCal(Year, Month)
    
# 默认日期
Year, Month = 2020,3
LabelCal(Year, Month)
  
button1 = tk.Button(root, text='Previous', command=ButtonPrevious)
button1.grid(row=8, column=0)
    
button2 = tk.Button(root, text='Next', command=ButtonNext)
button2.grid(row=8, column=6)

root.mainloop()