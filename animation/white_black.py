#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation

fig = plt.figure()
data = np.random.random((255,255))
im = plt.imshow(data, cmap='gray')

def animate(i):
    data = np.random.random((255,255))
    im.set_array(data)
    return [im]

anim = animation.FuncAnimation(fig, animate, frames=200, interval=60,blit=True)
anim.save('a.mp4', fps=20, writer='imagemagick', codec='libx264')
plt.show()
