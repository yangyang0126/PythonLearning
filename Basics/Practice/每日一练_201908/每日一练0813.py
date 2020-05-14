# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:52:30 2019

你需要创建一个带有两个参数的函数： 
（1）玩家的手中牌的列表 
（2）牌桌上当前 面朝上的牌

如果玩家可以进行游戏，则该函数将返回True;
如果玩家必须从牌组中抽取，则该函数将返回False。

如果有以下情况，玩家可以进行游戏： 
他们的卡片与面朝上卡片的颜色相同。 
他们的卡号与面朝上卡的号码相同。
"""
def solution(hand,face):
    color_face = face.split(" ")[0]
    number_face = face.split(" ")[1]
    for card in hand:
        color_hand = card.split(" ")[0]
        number_hand = card.split(" ")[1]
        if color_hand==color_face or number_hand==number_face:
            return True
    return False
print(solution(["yellow 3", "red 8"], "green 2"))

# 另一种算法
def solution(hand, face):
    for card in hand:
        if card[:4] in face or card[-1] in face:
            return True
    return False

print(solution(["yellow 3", "yellow 5", "red 8"], "red 2"))