# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 2019

@author: YangYang
"""


import easygui as g
import datetime
# 获取今天的日期
today = datetime.date.today()

# 判断日期是否合法
def is_date(date):
    try:
        datetime.datetime.strptime(date,"%Y-%m-%d")
        return True
    except:
        return False

#计算两个日期相差天数
def Caltime():
    msg = "请输入需要计算的日期"
    title = "计算两个日期的差"
    fieldNames = ["日期1", "日期2"]
    fieldValues = [today,today]  
    fieldValues = g.multenterbox(msg,title, fieldNames,values = fieldValues)
    while True:
        date1 = fieldValues[0]
        date2 = fieldValues[1]
        if is_date(date1) and is_date(date2):
            # 将字符串转为日期
            date1 = datetime.datetime.strptime(date1,"%Y-%m-%d")
            date2 = datetime.datetime.strptime(date2,"%Y-%m-%d")
            date_difference = date2-date1
            fieldNames.append("计算结果")
            fieldValues.append(date_difference.days)  
            msg = "计算结果"
            g.multenterbox(msg,title, fieldNames,values = fieldValues)
            break
        else:
            g.msgbox("日期格式输入错误，请重新输入")
            fieldValues = g.multenterbox(msg,title, fieldNames,values = fieldValues)

# 判断日期属于第几周星期几    
def Calcalendar():
    msg = "请输入需要计算的日期"
    title = "判断日期属于第几周星期几"
    fieldNames = ["日期"]
    fieldValues = [today]  
    fieldValues = g.multenterbox(msg,title, fieldNames,values = fieldValues)
    while True:
        date = fieldValues[0]       
        if is_date(date):            
            date = datetime.datetime.strptime(date,"%Y-%m-%d")
            fieldNames.append("计算结果")
            calendar = datetime.date.isocalendar(date)
            fieldValues.append("{}年第{}周星期{}".format(calendar[0],calendar[1],calendar[2]))  
            msg = "计算结果"
            g.multenterbox(msg,title, fieldNames,values = fieldValues)
            break
        else:
            g.msgbox("日期格式输入错误，请重新输入")
            fieldValues = g.multenterbox(msg,title, fieldNames,values = fieldValues)

# 判断日期是该年的第几天
def Caldays():
    msg = "请输入需要计算的日期"
    title = "判断日期是该年的第几天"
    fieldNames = ["日期"]
    fieldValues = [today]  
    fieldValues = g.multenterbox(msg,title, fieldNames,values = fieldValues)
    while True:
        date = fieldValues[0]       
        if is_date(date):   
            y,m,d=map(int,date.split("-"))
            D=0
            days=[31,0,31,30,31,30,31,31,30,31,30,31]
            if ((y%400==0)|((y%4==0)&(y%100!=0))):
                days[1]=29
            else:
                days[1]=28
            for i in range(m-1):
                D=D+days[i]
            fieldNames.append("计算结果")
            fieldValues.append("{}年第{}天".format(y,D+d))  
            msg = "计算结果"
            g.multenterbox(msg, title, fieldNames, values = fieldValues)
            break
        else:
            g.msgbox("日期格式输入错误，请重新输入")
            fieldValues = g.multenterbox(msg,title, fieldNames,values = fieldValues)

            
# 判断是否要继续计算    
def CalReply():    
    msg = "是否继续计算"
    choices = ["是","否"]
    reply = g.buttonbox(msg, choices=choices)
    if reply == "是":
        return True
    else:
        return False

# 选择需要计算的功能
def CalDate(choice): 
    if choice ==  "计算两个日期的差":
        Caltime()           
    if choice ==  "判断日期属于第几周星期几":
        Calcalendar()            
    if choice ==  "判断日期是该年的第几天":
        Caldays()
    Reply = CalReply()
    if Reply==True:
        choice = g.choicebox(msg, title, choices)
        CalDate(choice)
    else:
        return False
    return True

msg ="选择你需要的功能"
title = "日期计算"
choices = ["计算两个日期的差", "判断日期属于第几周星期几", "判断日期是该年的第几天"]
choice = g.choicebox(msg, title, choices)
CalDate(choice)


