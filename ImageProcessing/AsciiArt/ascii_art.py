# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:32:30 2019

@author: Administrator
"""

from ascii_art import ASCIIArt, ASCIIPicture

picture = ASCIIArt('img', 5).draw_ascii(curve=1)
ASCIIPicture(picture).save('cat_scale5_draw_ascii.png')

colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.FULL_RANGE, curve=1.5)
ASCIIPicture(colored_picture).save('cat_scale5_full_range_color.png')

with open('cat_scale5_draw.txt', 'w') as f:
    f.write(''.join(picture))