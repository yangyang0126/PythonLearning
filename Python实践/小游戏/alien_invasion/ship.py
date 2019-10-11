# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:45:49 2019

@author: Administrator
"""

import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """初始化飞船，设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像，获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # 获取属性rect
        self.screen_rect = screen.get_rect()
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx # center 、centerx 或centery
        self.rect.bottom = self.screen_rect.bottom # top 、bottom 、left 或right
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 根据self.cneter更新rect对象
        self.rect.centerx = self.center
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
        
