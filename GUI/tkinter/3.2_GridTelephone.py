# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:00:52 2020
@author: Yenny
"""

from tkinter import *
root = Tk()
labels = [['1','2','3'], # 文本，布局为网格
          ['4','5','6'],
          ['7','8','9'],
          ['*','0','#']]

for r in range(4): # 行循环
    for c in range(3): # 列循环
        label = Label(root,
                      relief=RAISED, # 设置边框格式
                      padx=10, # 加宽标签
                      text=labels[r][c]) # 标签文本
        label.grid(row=r, column=c) # 将标签放置在r行c列

root.mainloop()