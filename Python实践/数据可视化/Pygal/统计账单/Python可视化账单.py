# -*- coding: utf-8 -*-
"""
Created on Thu May 30 2019

@author: YangYang
"""
import pygal  
import pandas as pd
import math

# 输出各项支出统计
def PlotItems(df):
    dot_chart = pygal.Dot(x_label_rotation=30)
    #line_chart.title = '每月支出'
    for i in range(0,4):         
        data=df.ix[i].values
        for j in range(2,14):                 
            if math.isnan(data[j]):    
                data[j] = 0          
        dot_chart.add(df.ix[i,1], data[2:len(data)])
    dot_chart.x_labels = map(str, range(1, 13))
    dot_chart.render_to_file("部分支出情况.svg")
    

# 统计各项支出汇总
def SumItems(df,n):
    data=df.ix[n].values
    items = 0
    for i in range(2,14):   
        #  判断Excel表格中的空值nan
        if math.isnan(data[i]):    
            data[i] = 0
        items += float(data[i])    
    return items

# 统计预算进度
def CalBudget(df):
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=pygal.style.styles['default'](value_font_size=10))
    percent_formatter = lambda x: '{:.10g}%'.format(x)    
    gauge.value_formatter = percent_formatter
    #gauge.title = '各项预算进度(%)'
    for i in range(0,len(df)-1): 
        data=df.ix[i].values
        items = SumItems(df,i)        
        items = round(items/data[0]*100,2)    
        gauge.add(df.ix[i,1], items)
    gauge.render_to_file("各项预算进度.svg")

# 统计预算总进度
def CalBudgetTotel(df):
    gauge = pygal.SolidGauge(inner_radius=0.70)
    percent_formatter = lambda x: '{:.10g}%'.format(x)    
    gauge.value_formatter = percent_formatter
    #gauge.title = '年度预算进度(%)'
    i = len(df)-1
    data=df.ix[i].values
    items = SumItems(df,i)        
    items = round(items/data[0]*100,2)    
    gauge.add(df.ix[i,1],items)
    gauge.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
    gauge.render_to_file("年度预算进度.svg")
    
def CalPie(df):    
    pie_chart = pygal.Pie(inner_radius=.4)
    #pie_chart.title = '支出分类'
    for i in range(0,len(df)-1):         
        items = SumItems(df,i)           
        pie_chart.add(df.ix[i,1], items)
    pie_chart.render_to_file("支出分类.svg")

# 统计所有支出
def CalTotal(df):
    line_chart = pygal.StackedBar()
    #line_chart.title = '每月支出'
    for i in range(0,len(df)-1):         
        data=df.ix[i].values
        for j in range(2,14):                 
            if math.isnan(data[j]):    
                data[j] = 0          
        line_chart.add(df.ix[i,1], data[2:len(data)])
    line_chart.x_labels = map(str, range(1, 13))
    line_chart.render_to_file("年度支出柱状图.svg")
    
# 读取表格数据
df = pd.read_excel('家庭支出清单.xlsx')  #默认读取到Excel的第一个表单
PlotItems(df)  #你可以根据需求，画出你要的各项单独统计
CalBudget(df)  # 各项目预算情况 
CalBudgetTotel(df)  # 年度预算情况 
CalPie(df)  #支出分类
CalTotal(df)  #年度支出柱状图