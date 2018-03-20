#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure()
axes1 = fig.add_subplot(1,1,1)
line, =axes1.plot(np.random.rand(10))

def update(data):
    line.set_ydata(data)
    return line,
def data_gen():
    while True:
        # line, = axes1.plot(np.random.rand(10))
        # return line,
        yield np.random.rand(10)

ani = animation.FuncAnimation(fig, update, data_gen(),interval=2*1000)
plt.show()
