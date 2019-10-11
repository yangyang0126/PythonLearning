# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 11:10:31 2019

创建一个函数，该函数反转字符串中的字母，但保持当前顺序的数字。
"""
def solution(txt):
    txt = list(txt)
    letter = []
    for t in txt:
        if t.isalpha():
            letter.append(t)
    j = len(letter)
    for i in range(len(txt)):
        if txt[i].isalpha():
            txt[i] = letter[j-1]
            j = j-1
    return ("".join(txt)) 
print(solution("ab89c"))

#另一种方法
def solution(txt):
	letters=[i for i in txt if i in 'abcdefghijklmnopqrstuvwxyz']
	letters=letters[::-1]
	ans=''
	step=0
	for i in range(len(txt)):
		if txt[i] in letters: 
			ans+=letters[step]
			step+=1
		else: ans+=txt[i]
	return ans

print(solution("123a45"))