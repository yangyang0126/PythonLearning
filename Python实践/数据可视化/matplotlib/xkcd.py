# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:28:43 2019

@author: Administrator

https://matplotlib.org/gallery/showcase/xkcd.html
"""

import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 10])
    
    data = np.ones(100)
    data[70:] -= np.arange(30)
    
    ax.annotate(
            'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
            xy = (70,1), arrowprops = dict(arrowstyle= '->'), xytext=(15, -15))
    
    ax.plot(data)
    
    ax.set_xlabel('time')
    ax.set_ylabel('my overall health')
    fig.text(
            0.5, 0.05,
            '"Stove Ownership" from xkcd by Randall Munroe',
            ha = 'center')