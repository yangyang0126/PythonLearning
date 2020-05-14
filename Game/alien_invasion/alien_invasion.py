# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:07:21 2019

@author: Administrator
"""


import pygame  # pygame模块包含开发游戏所需要的功能

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并建立一个屏幕对象
    pygame.init()  #初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  #  screen = pygame.display.set_mode((1200, 800)) #创建显示窗口，宽1200像素，高800像素
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
 
    

    
    #开始游戏的主循环
    while True:
        
       gf.check_events(ship)
       ship.update()
       gf.update_screen(ai_settings, screen, ship)


run_game()
