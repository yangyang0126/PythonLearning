# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:02:59 2020
@author: Yenny
"""

from tkinter import *
from tkinter.messagebox import showinfo
import datetime

def clicked():
    day = datetime.datetime.now().strftime('%d %b %Y')
    time = datetime.datetime.now().strftime('%H:%M:%S %p')
    text = 'Day：'+day+'\n'+'Time：'+time+'\n'
    showinfo(message=text)

root = Tk()

botton = Button(root,
                text='Click it',
                command=clicked)
botton.pack()
root.mainloop()