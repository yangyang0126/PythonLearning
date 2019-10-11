# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:59:59 2019

@author: Administrator
"""

# 引入日历模块
import calendar
import datetime
 

# 输入指定年月
yy = datetime.date.today().year 
mm = datetime.date.today().month
  
CalendarTitle = calendar.month(yy,mm).split('\n', 1)[0]
