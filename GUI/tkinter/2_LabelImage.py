# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:58:07 2020
@author: Yenny
"""

from tkinter import *
root = Tk()
photo = PhotoImage(file='cake.png') # 将图片转化为tkinter可以显示的格式
hello = Label(master=root,
              image=photo,
              width=300, # 标签宽度，以像素为单位
              height=180) # 标签高度，以像素为单位
hello.pack()
root.mainloop()