# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:22:59 2019

@author: Administrator
"""

class Settings():
    """储存《外星人入侵》的所有设置"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200  # 宽1200像素
        self.screen_height = 600  # 高600像素
        self.bg_color = (230, 230, 230)  # 设置背景色,浅灰色

        # 飞船的设置
        self.ship_speed_factor = 1.5