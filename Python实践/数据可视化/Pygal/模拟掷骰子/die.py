# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:43:24 2019

@author: Administrator
"""

from random import randint

class Die():
    
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, self.num_sides)
    