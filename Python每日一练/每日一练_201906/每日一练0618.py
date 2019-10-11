# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:21:23 2019

@author: Administrator
"""

def flashcard(x,sym,y):
    cal = x + sym + y
    return eval(cal)
print(flashcard("2","*","3"))    