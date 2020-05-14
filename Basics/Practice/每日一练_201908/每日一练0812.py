# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 09:58:26 2019

@author: Administrator
"""

def solution(s):
    s_count = []
    word = []
    count_word = []
    for i in s:
        word.append(i)
        count_word.append(s.count(i))
    s_zip = zip(word,count_word)
    s_zip = sorted(s_zip)
    s_temp = {key:value for key,value in s_zip}
    for key,value in s_temp.items():
        s_count.append(str(key))
        s_count.append(str(value))        
    return ("".join(s_count))
print(solution('cccddecca'))
print(solution('dabcab'))
print(solution('aacbac'))

# 优化版
def solution(s):
    return "".join([i+str(s.count(i)) for i in sorted(set(s))]) 
   
print(solution('cccddecca'))
print(solution('dabcab'))
print(solution('aacbac'))
