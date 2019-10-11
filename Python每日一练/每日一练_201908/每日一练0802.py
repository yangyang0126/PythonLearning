# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:15:31 2019

注册邮箱时建立的新密码只有满足一些规则后才能创建成功。
请你创建一个验证密码的函数，以符合以下规则：

长度在 6 到 24 个之间。 至少一个大写字母（ A-Z ）。
至少一个小写字母（ a-z ）。 至少一个数字（ 0-9 ）。 
最多 2 个重复字符：“aa” 可以；“aaa” 不行。 
支持的特殊字符：！ @＃$％^＆*（）+ = _ - {} [] :; “'？ <> ,.
"""

# 作业
def solution(password):
    if len(password)>24 or len(password)<6:
        return False
    for p in password:       
        if p.isdigit():
            p_digit = True
            break
        else:
            p_digit = False
    for p in password:        
        if p.islower():
            p_lower = True
            break
        else:
            p_lower = False
    for p in password:       
        if p.isupper():
            p_upper = True
            break
        else:
            p_upper = False
    if p_digit==p_lower==p_upper==False:
        if not (p in "！ @＃$％^＆*（）+ = _ - {} [] :; “'？ <> ,."):
            return False
    
    for i in range(len(password)-2):
        if password[i] == password[i+1] and password[i+1] == password[i+2]:
            return False
        
    if p_digit==p_lower==p_upper==True:
        return True    
    else:
        return False

print(solution("iLoveYou"))

# 参考答案
def solution(password):
	count1 = 0
	count2 = 0
	count3 = 0
	if len(password) < 6 or len(password) > 24:
		return False
	for ch in password:
		if ch.isupper():
			count1 += 1
		if ch.islower():
			count2 += 1
		if ch.isdigit():
			count3 += 1
	if count1 < 1 or count2 < 1 or count3 < 1:
		return False
	for i in range(len(password)-2):
		if password[i] == password[i+1] and password[i+1] == password[i+2]:
			return False
	return True

print(solution('iLoveYou'))