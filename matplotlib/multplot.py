#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
x=[1,2,3,4]
y=[2,3,4,5]
ax1.plot(x,y,'o',color='r')
ax1.set_title('Simple figure')

ax2 = fig.add_subplot(1,2,2)
x=[1,2,3,4]
y=[2,3,4,5]
ax2.plot(x,y,'*',color='b')
ax2.set_title('Simple figure')

fig.savefig('../savefig/multplot.png')

plt.show()
