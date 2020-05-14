# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:21:04 2019

@author: Administrator
"""

#七段数码管绘制
import turtle
import time
 
def drawGap(): #控制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):#绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.rt(90)
 
def drawDigit(digit):#根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in  [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in  [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.lt(90)
    drawLine(True) if digit in  [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in  [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in  [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.lt(180)
    turtle.penup()
    turtle.fd(20)
 
def drawDate(date): #获得需要输出的数字 %Y-%m=%d+
    turtle.pencolor('red')
    for i in date:
        if i=='-':
            turtle.write('年',font=('Arial',24,'normal'))
            turtle.pencolor('yellow')
            turtle.fd(40)
        elif i=='=':
            turtle.write('月',font=('Arial',24,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i=='+':
            turtle.write('日',font=('Arial',24,'normal'))
        else:
            drawDigit(eval(i))
 
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
 
main()