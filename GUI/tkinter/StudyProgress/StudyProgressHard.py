# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:21:26 2020
@author: Yenny
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:50:05 2020

@author: zhaoy
"""

import ShanbeyRecord
import tkinter as tk
from tkinter.messagebox import showinfo
import time 

window = tk.Tk()  # 创建主窗口
window.title('Progress')  # 窗口名称
window.geometry('700x450')  # 窗口大小

bgcolor = '#F0FFF0'#'lightcyan' # 背景颜色
fgcolor = 'teal'  #前景颜色
window.configure(background=bgcolor)  # 给窗口上色

# 显示标题
tk.Label(window, text='2020', background=bgcolor, font=('Helvetica',40,'bold italic'), foreground=fgcolor).place(x=280, y=30)

# 显示输入信息框
tk.Label(window, text='Your Goal (Every Day)', background=bgcolor, font=('Helvetica',14,'bold italic'), foreground=fgcolor).place(x=50, y=120)
tk.Label(window, text='Shanbey ID', background=bgcolor, font=('Helvetica',14,'bold italic'), foreground=fgcolor).place(x=50, y=170)
#
EntWord = tk.Entry(window, textvariable=tk.StringVar(value='word number'), width=12, fg=fgcolor, font=('Helvetica',10,'italic'))
EntWord.place(x=300, y=125)
EntRead = tk.Entry(window, textvariable=tk.StringVar(value='read number'), width=12, fg=fgcolor, font=('Helvetica',10,'italic'))
EntRead.place(x=425, y=125)
EntListen = tk.Entry(window, textvariable=tk.StringVar(value='listen number'), width=12, fg=fgcolor, font=('Helvetica',10,'italic'))
EntListen.place(x=550, y=125)
EntID = tk.Entry(window, textvariable=tk.StringVar(value='ID：must be number'), width=20, fg=fgcolor, font=('Helvetica',10,'italic'))
EntID.place(x=180, y=175)
#
# 设置进度条标签
tk.Label(window, text='Word', background=bgcolor, font=('Helvetica',16,'bold italic'), foreground=fgcolor).place(x=50, y=100+150)
tk.Label(window, text='Read', background=bgcolor, font=('Helvetica',16,'bold italic'), foreground=fgcolor).place(x=50, y=150+150)
tk.Label(window, text='Listen', background=bgcolor, font=('Helvetica',16,'bold italic'), foreground=fgcolor).place(x=50, y=200+150)
#
# 设置进度条
CanvasWord = tk.Canvas(window, width=465, height=22, bg="white")
CanvasWord.place(x=120, y=100+150)
CanvasRead = tk.Canvas(window, width=465, height=22, bg="white")
CanvasRead.place(x=120, y=150+150)
CanvasListen = tk.Canvas(window, width=465, height=22, bg="white")
CanvasListen.place(x=120, y=200+150)
#
# 显示进度条
def ShowProgress(canvas, number, total):
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill=fgcolor)
    x = total  # 未知变量，可更改
    n = 465/x  # 465是矩形填充满的次数
    for i in range(number):
        n = n + 465/x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(1/number)  # 控制进度条流动的速度
        
def Start():
    # 获取输入的每天目标
    GoalWord = EntWord.get()
    GoalRead = EntRead.get()
    GoalListen = EntListen.get() 
    
    # 判断是不是输入的是数字，如果不是，窗口提示
    try:
        NumWord = int(GoalWord)
        NumRead = int(GoalRead)
        NumListen = int(GoalListen)
    except:
        showinfo(message='每月目标输入错误，请输入纯数字')
        return False
    
    # 一年有365天
    GoalWord = NumWord*365
    GoalRead = NumRead*365
    GoalListen = NumListen*365
    
    # 获取目标值
    tk.Label(window, text=str(GoalWord), background=bgcolor, font=('Helvetica',13,'bold italic'), foreground=fgcolor).place(x=590, y=100+150)
    tk.Label(window, text=str(GoalRead), background=bgcolor, font=('Helvetica',13,'bold italic'), foreground=fgcolor).place(x=590, y=150+150)
    tk.Label(window, text=str(GoalListen), background=bgcolor, font=('Helvetica',13,'bold italic'), foreground=fgcolor).place(x=590, y=200+150)
#
    # 读取扇贝数据    
    ID = EntID.get()
    
    try:
        ShanbeyRecord.ReadRecond(int(ID))
        Record = ShanbeyRecord.ReadRecond(ID)
        Word = Record.Word
        Read = Record.Read
        Listen = Record.Listen        
    except:
        showinfo(message='ID输入错误，请输入纯数字\n'+
                 '可通过扇贝网页版，右上角【我的打卡】，获取打卡网址\n'+
                 '网址是https://www.shanbay.com/checkin/user/*******/\n'+
                 '最后一串数字即为ID')
        return False
#        
    ShowProgress(CanvasWord, Word, GoalWord)
    ShowProgress(CanvasRead, Read, GoalRead)
    ShowProgress(CanvasListen, Listen, GoalListen)
#
# button按钮
# relief must be flat, groove, raised, ridge, solid, or sunken
StartButton = tk.Button(window, 
                        text='Let Go!', 
                        font=('Helvetica',14,'bold italic'), 
                        foreground=fgcolor,                         	
                        background=bgcolor,
                        activebackground='white',
                        activeforeground=fgcolor,
                        relief='raised',
                        command=Start)
StartButton.place(x=550, y=160)

window.mainloop()