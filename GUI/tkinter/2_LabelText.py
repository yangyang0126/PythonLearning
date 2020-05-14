# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:56:54 2020
@author: Yenny
"""

from tkinter import *
root = Tk()
hello = Label(master = root, text = "Hello GUI world!") # 创建Label对象
hello.pack() # 放置于父组件的顶部中心
root.mainloop()