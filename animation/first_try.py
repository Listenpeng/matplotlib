#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
xdata = []
ydata = []
line, = plt.plot([], [], '-', animated=True)

def init():
    ax.set_xlim(0, 10 * np.pi)
    ax.set_ylim(-1.1, 1.1)
    return line,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig,update,frames=np.linspace(0, 10 * np.pi, 500),
                              init_func=init, blit=True, interval=10)

plt.show()
