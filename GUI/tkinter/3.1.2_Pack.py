# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:59:53 2020
@author: Yenny
"""

from tkinter import *
root = Tk()
text = Label(root,
             font=('Helvetica',16,'bold italic'), # 设置字体，加粗、斜体、大小16点                
             foreground='white', # 字体颜色
             background='black', # 背景颜色
             padx=25, # 标签左右扩展25像素
             pady=50, # 标签上下扩展10像素
             text='This is my painting.\n It is a cake.')
text.pack(side=LEFT) # 标签放在下方

cake = PhotoImage(file='cake.png')
cakeLabel = Label(root,
                  image=cake, 
                  background='white', 
                  width=150,
                  height=150,
                  borderwidth=3, # 设置标签边框宽度
                  relief=RIDGE) # 设置标签边框样式：隆起
cakeLabel.pack(side=RIGHT) # 标签放在左侧

root.mainloop()