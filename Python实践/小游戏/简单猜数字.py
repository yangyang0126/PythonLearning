# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:37:44 2019

@author: Administrator
"""

import easygui
import random
number = random.randint(1,99)
guess = 0
tries = 0

easygui.msgbox("一起来猜数字，范围是1-99，给你6次机会哟")
while guess != number and tries < 10:
    guess = easygui.integerbox("输入你猜想的数字：")
    if guess > number:
        easygui.msgbox("你猜的数字"+str(guess)+"太大啦")
    elif guess < number:
        easygui.msgbox("你猜的数字"+str(guess)+"太小啦")
    else:        
        break
    tries += 1
if guess == number:
    easygui.msgbox("猜对啦！")
else:
    easygui.msgbox("猜测次数到，你失败啦")