# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:51:52 2019

@author: Administrator
"""

"""
输入两组字符串，判断他们的样式是否相同
abab 和 caca : True
abced 和 vwxyz ：True
accab 和 acb ：False
aabb 和 abab : False
"""


# 判断字母的位置
def findletter(letter,word):
    count = 0
    count_list = []
    for w in word:
        count += 1
        if w == letter:
            count_list.append(count-1)
    return count_list

def judge(word1,word2):
    if len(word1) != len(word2):
        return False
    else:
        for i in range(len(word1)):
            location1 = findletter(word1[i],word1)
            location2 = findletter(word2[i],word2)
            if location1 != location2:
                return False            
    return True

print(judge("abab","caca"))
print(judge("abced","vwxyz"))
print(judge("accab","acb"))
print(judge("aabb","abab"))
