# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:12:55 2019

@author: Administrator
"""

def decision(cards,face_up_card):
    # 确定对面上家出牌的颜色和数字
    face_up_color = face_up_card.split(" ")[0]
    face_up_number = face_up_card.split(" ")[1]
    
    # 确认你手中的牌
    for card in cards:
        if card.split(" ")[0] == face_up_color or card.split(" ")[1] == face_up_number:
            cards.remove(card)
            break
    # 判断    
    if len(cards) == 1:
        print ("Uno!")
    elif len(cards) == 0:
        print ("You win!")
    else:
        print ("keep going...")
    
decision(["yellow 3","red 3"],"red 10")    
decision(["blue 1"],"blue 10")    
decision(["blue 1","green 2","yellow 4","red 2"],"blue 5") 