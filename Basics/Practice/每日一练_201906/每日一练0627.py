# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:34:41 2019

@author: Administrator
"""
# 这个函数用不上，可以判断所有字母的位置
def findletter(letter,word):
    count = 0
    count_list = []
    for w in word:
        count += 1
        if w == letter:
            count_list.append(count-1)
    return count_list

def judgestr(word,word_ref):
    for i in word:
        loc = word_ref.find(i)
        if  loc == -1:
            return False
        else:
            word_ref = word_ref[loc+1:]
    return True

        
word_ref = "beautiful"
word = "betul"
print(judgestr(word,word_ref))

