#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

def scatter1():
    x= np.array([x for x in range(1,21)])
    y= x**2
    colors=['green','yellow','blue','red','orange','purple','cyan']
    random_colors=random.sample(colors,7)
    fig=plt.figure()
    plt.scatter(x, y, s=100, c=random_colors, alpha=0.8)
    plt.savefig('../savefig/color_scatter1.png')
    plt.show()

scatter1()

def scatter3():
    N = 80
    colors = ['green', 'yellow', 'blue', 'red',
              'orange', 'purple', 'cyan']
    random_colors = random.sample(colors, 7)
    x = np.random.rand(N)
    y = np.random.rand(N)
    area = np.pi * (15* np.random.rand(N))**2
    plt.scatter(x, y, s=area, c=random_colors, alpha=0.8)
    plt.savefig('../savefig/color_scatter3.png')
    plt.show()

scatter3()
