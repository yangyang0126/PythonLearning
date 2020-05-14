# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:46:39 2019

为了督促学生们锻炼身体，学校在校园里放置来4个打卡器，
要求每人每日至少打卡两次。每天打卡器会传回一些数据
，请你写一个函数，找出没有完成锻炼的学生。

solution('王萌萌','扇小贝', '王萌萌', '林小米','林小米','晨','王萌萌','晨']) ➞ [‘扇小贝’]

solution([‘安琪’,'小鱼','小鱼','奇一','小鱼']) ➞ ['安琪', '奇一']
"""
# 作业
def solution(lst):
    name_unfinished = []
    for name in lst:
        if lst.count(name)<2:
            name_unfinished.append(name)
    return name_unfinished

print(solution(['王萌萌','扇小贝', '王萌萌', '林小米','林小米','晨','王萌萌','晨']))

