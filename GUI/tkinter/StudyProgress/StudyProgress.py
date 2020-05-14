# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:10:23 2020

@author: zhaoy
"""
import ShanbeyRecord
import tkinter as tk
import time 

window = tk.Tk()  # 创建主窗口
window.title('Progress')  # 窗口名称
window.geometry('700x450')  # 窗口大小

bgcolor = 'lightcyan' # 背景颜色
fgcolor = 'teal'  #前景颜色
window.configure(background=bgcolor)  # 给窗口上色

# 显示标题
tk.Label(window, text='2020', background=bgcolor, font=('Helvetica',40,'bold italic'), foreground=fgcolor).place(x=260, y=20)

# 设置进度条标签
tk.Label(window, text='Word', background=bgcolor, font=('Helvetica',16,'bold italic'), foreground=fgcolor).place(x=30, y=100)
tk.Label(window, text='Read', background=bgcolor, font=('Helvetica',16,'bold italic'), foreground=fgcolor).place(x=30, y=150)
tk.Label(window, text='Listen', background=bgcolor, font=('Helvetica',16,'bold italic'), foreground=fgcolor).place(x=30, y=200)

tk.Label(window, text='7300个', background=bgcolor, font=('Helvetica',10,'bold italic'), foreground=fgcolor).place(x=590, y=100)
tk.Label(window, text='730篇', background=bgcolor, font=('Helvetica',10,'bold italic'), foreground=fgcolor).place(x=590, y=150)
tk.Label(window, text='1825句', background=bgcolor, font=('Helvetica',10,'bold italic'), foreground=fgcolor).place(x=590, y=200)


# 设置进度条
CanvasWord = tk.Canvas(window, width=465, height=22, bg="white")
CanvasWord.place(x=110, y=100)
CanvasRead = tk.Canvas(window, width=465, height=22, bg="white")
CanvasRead.place(x=110, y=150)
CanvasListen = tk.Canvas(window, width=465, height=22, bg="white")
CanvasListen.place(x=110, y=200)

# 读取扇贝数据
ID = 16888030   
Record = ShanbeyRecord.ReadRecond(ID)     
Word = Record.Word
Read = Record.Read
Listen = Record.Listen
 
# 显示进度条
def ShowProgress(canvas, number, total):
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill=fgcolor)
    x = total  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数
    for i in range(number):
        n = n + 465 / x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(1/number)  # 控制进度条流动的速度
    
ShowProgress(CanvasWord, Word, 7300)
ShowProgress(CanvasRead, Read, 730)
ShowProgress(CanvasListen, Listen, 1825)

window.mainloop()
