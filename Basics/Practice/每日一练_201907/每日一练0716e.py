# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:54:45 2019

@author: Administrator
"""

def solution(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    return(pin.isdigit())

print(solution('1234'))