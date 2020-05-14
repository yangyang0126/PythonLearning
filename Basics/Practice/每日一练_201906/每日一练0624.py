# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:38:19 2019

@author: Administrator
"""

"""
如果一个单词中的每个字母都不一样
我们成为isogram
判断一个单词是不是isogram
如果是，输出True
如果不是，输出False

"""
import re
Word = "usually"
def isogram(Word):    
    for i in Word:
        loction = re.findall(i,Word)
        if len(loction) > 1:
            return False 
    return True
print(isogram(Word))