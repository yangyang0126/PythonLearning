# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 2019

@author: YangYang
"""
"""
成绩>=90，是A
成绩60-89之间，是B
成绩60以下，是C
"""

StudentScore = [90,80,75,50]
UpdateScore = []
for score in StudentScore:
    if score >= 90:
        UpdateScore.append("A")
    elif score >= 60 and score <= 89:
        UpdateScore.append("B")
    else:
        UpdateScore.append("C")
print(UpdateScore)
        
        