#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
#生成一个50以内的随机数列表
x= [x for x in range(50)]
#颜色的列表
colors = ['r','y','g','b','c','m']
#标志的字典
legends={'circle':'o','star':'*','triangle_down':'v',
         'dash-dot':'-.','dashed_line':'--','x_mark':'x'}
plt.yticks([y for y in range(-7,20,2)])
#enumerate 列举
for index,t in enumerate(legends.values()):
    sample_y=np.random.randn(50).cumsum()
    plt.plot(x,sample_y,t,color=colors[index])

plt.legend(legends.keys(),loc=2)
plt.savefig('../savefig/mult_dot.png')
plt.show()
