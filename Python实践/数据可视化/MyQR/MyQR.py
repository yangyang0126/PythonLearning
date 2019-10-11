# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:35:28 2019

@author: Administrator
"""

from MyQR import myqr
myqr.run(words='https://www.jianshu.com/u/14fcbd93e233',   # 二维码显示的网址      
         picture = 'img1.jpg',# 参考图片或者动图（不写的话，就是默认的）
         colorized = True # 是否要彩色的
         )