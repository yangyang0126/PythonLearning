# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:56:57 2020
@author: Yenny
"""

#from removebg import RemoveBg
#
#rmbg = RemoveBg("D******F", "error.log")
#rmbg.remove_background_from_img_file("remove1.jpg")


# 填充背景色
#from PIL import Image
#im = Image.open('remove1.jpg_no_bg.png')
#x, y = im.size
#try:    
#    p = Image.new('RGBA', im.size, (64, 128, 128))
#    p.paste(im, (0, 0, x, y), im)    
#    p.save('remove1.jpg_color_bg.png')
#except:
#    with open('./error.log', 'a') as f:
#        f.write('background change fail .')



from removebg import RemoveBg
import os

rmbg = RemoveBg("D******F", "error.log")

#图片放到程序的同级文件夹 picture 里面
path = '%s/picture'%os.getcwd() 

for pic in os.listdir(path):
	rmbg.remove_background_from_img_file("%s\%s"%(path,pic))
