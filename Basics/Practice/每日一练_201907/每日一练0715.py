# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:39:43 2019

@author: YangYang

设计一个抽奖活动，
输入参与人数、参与人姓名、参与人ID，
输入中奖人名单

需要先安装faker库： pip install faker
"""

from faker import Faker
import random

fake = Faker(locale = 'zh_CN')

n = input("请输入参与人数：")
m = input("请输入中奖人数：")

# 构造ID和人名
list_name = []
list_ID = list(range(0,int(n)))
for _ in range(int(n)):
  list_name.append(fake.name())

# 开始抽奖
print("\n")
print("中奖名单：")
for _ in range(int(m)):
    ID_random = random.choice(list_ID)
    print("ID：{}，{}".format(ID_random, list_name[ID_random]))
    list_name.remove(list_name[ID_random])