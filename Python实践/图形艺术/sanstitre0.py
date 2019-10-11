# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:24:59 2019

@author: Administrator
"""

import easygui as g
from MyQR import myqr


# 二维码生成器
def PrintMyqr():
    IsPicture = False
    web = 'https://www.jianshu.com/u/14fcbd93e233'
    if IsPicture == True:
        picture='timg.gif'
        colorized=True
        myqr.run(words = web,   # 二维码显示的网址      
                 picture = picture,# 参考图片或者动图（不写的话，就是默认的）
                 colorized = colorized # 是否要彩色的
                 )
    else:
        myqr.run(words = web)   # 二维码显示的网址     

# Ascii图生成器
def PrintAsciiArt():
    from ascii_art import ASCIIArt, ASCIIPicture

    picture = ASCIIArt('cat', 5).draw_ascii(curve=1)
    ASCIIPicture(picture).save('cat_scale5_draw_ascii.png')
    
    colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.FULL_RANGE, curve=1.5)
    ASCIIPicture(colored_picture).save('cat_scale5_full_range_color.png')
    
    with open('cat_scale5_draw.txt', 'w') as f:
        f.write(''.join(picture))               
                 
# image = "python_and_check_logo.gif"
title = "图形艺术"
msg = "请选择你需要的功能"
choices = ["艺术二维码","图像迭代","No opinion"]
reply = g.buttonbox(msg,title,
                  #image=image,
                  choices=choices
               )
if reply == "艺术二维码":
    PrintMyqr()
