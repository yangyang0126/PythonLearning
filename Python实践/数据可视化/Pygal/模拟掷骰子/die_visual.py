# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:46:44 2019

@author: Administrator
"""

from die import Die

die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
    
print(results)