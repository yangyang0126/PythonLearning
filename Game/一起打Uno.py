# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:12:55 2019

@author: Administrator
"""
# 生成UNO牌，40张
import random
card_color = ["red","yellow","green","blue"]
card_number = list(range(0,10))
cards_totel = [str(i)+" "+str(j) for i in card_color for j in card_number]

# 给对家随机发10张牌
cards_play = []
cards_play.append(random.sample(cards_totel,10))
# 去除重复值，给自己发10张牌
for card in cards_play[0]:
    cards_totel.remove(card)
cards_play.append(random.sample(cards_totel,10)) 
for card in cards_play[1]:
    cards_totel.remove(card)

# 制定打牌规则
def decision(cards,face_up_card,member):
    # 确定对面上家出牌的颜色和数字
    face_up_color = face_up_card.split(" ")[0]
    face_up_number = face_up_card.split(" ")[1]
    
    # 确认你手中的牌
    cards_temp = []
    for card in cards:
        if card.split(" ")[0] == face_up_color or card.split(" ")[1] == face_up_number:
            cards_temp.append(card)
    
    # 如果你没牌可出
    if cards_temp == []:
        
        card_temp = face_up_card
        choose = 0
        card_add = 1
        game_over = 0
        
    # 你可以出牌
    else:
        card_temp = random.choice(cards_temp)    
        cards.remove(card_temp)
        card_add = 0 #不加牌
        game_over = 0
        choose = 1   
    # 判断    
        if len(cards) == 1:
            print (member+": "+card_temp +":"+" Uno!")                    
        elif len(cards) == 0:
            print (member+": "+card_temp+":"+" 赢啦!")            
            game_over = 1
        else:
            print (member+": "+card_temp)   
    
    return cards,card_temp,choose,card_add,game_over
 
# 开始打牌，对家先出牌
member = ["York","Grit"]
face_up_card =  random.choice(cards_play[0])   
print(member[0]+" :"+face_up_card)
cards_play[0].remove(face_up_card)
choose = 1 # 判断游戏要不要玩下去 
play = 0 # 选择玩家1号还是玩家2号
card_add = 0 # 无牌可出，抽牌
for i in range(1000): 
    if choose == 1:
        if play == 0:   
            play = 1            
        else:    
            play = 0
        [cards_play[play],face_up_card,choose,card_add,game_over] = decision(cards_play[play],face_up_card,member[play]) 
        if game_over == 1:
            break    
    else:
        if card_add == 1: # 抽牌
            if cards_totel == []:
                print("游戏死局")
                break
            else:
                card_r = random.choice(cards_totel)
                cards_totel.remove(card_r)
                print (member[play]+": "+"无牌可出，抽牌 "+card_r)
                cards_play[play].append(card_r) 
                [cards_play[play],face_up_card,choose,card_add,game_over] = decision(cards_play[play],face_up_card,member[play]) 
     
input("游戏结束")
