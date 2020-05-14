# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:01:31 2020
@author: Yenny
"""

import calendar 
from tkinter import *
root = Tk()
labels = [['Mon','Tue','Wed','Thu','Fri','Sat','Sun']]
MonthCal = calendar.monthcalendar(2020, 3)
for i in range(len(MonthCal)):
    labels.append(MonthCal[i])
for r in range(len(MonthCal)+1):
    for c in range(7):
        if labels[r][c] == 0:
            labels[r][c] = ' '
        label = Label(root,          
                      padx=5,
                      pady=5,
                      text=str(labels[r][c]))        
        label.grid(row=r,column=c)
root.mainloop()