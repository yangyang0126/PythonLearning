# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:21:53 2020

@author: admin
"""

import turtle as t

def hair():    # 画头发
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    for j in range(10):                   # 重复执行10次
        t.setheading(60 - (j * 36))       # 每次调整初始角度
        t.circle(-50, 120)                # 画120度的弧
    t.end_fill()

def face():    # 画脸
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.setheading(180)
    t.circle(85)
    t.end_fill()
    #下巴
    t.circle(85, 120)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(85, 120)
    t.setheading(135)
    t.circle(100, 95)
    t.end_fill()
    
def ears(dir):    # 画眼睛，dir用来设置方向，左右眼对称
    t.penup()
    t.goto((0-dir)*30, 90)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.circle(dir*30)
    t.end_fill()
    
    t.penup()
    t.goto((0-dir)*40, 85)
    t.setheading(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir*17)
    t.end_fill()
    
def nose():    # 画鼻子
    t.penup()
    t.goto(20, 0)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
def eye(dir):    # 画耳朵，dir用来设置方向，左右耳对称
    t.penup()
    t.goto((0-dir)*30, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def mouth():    # 画嘴巴
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.forward(50)
    t.setheading(0)
    t.circle(80, 30)
    t.penup()
    t.goto(0, -50)
    t.setheading(180)
    t.pendown()
    t.circle(-80, 30)   
    
hair()
ears(1)
ears(-1)
face()
eye(1)
eye(-1)
mouth()
nose()
t.done()