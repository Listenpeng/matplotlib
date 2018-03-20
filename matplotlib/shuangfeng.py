#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x,y = np.mgrid[-2:2:20j, -2:2:20j]
z = x*np.exp(-x**2-y**2)

ax = plt.subplot(111, projection='3d')
ax.plot_surface(x,y,z, label='z=xe^-x**2-y**2',rstride=3, cstride=1, cmap=plt.cm.coolwarm, alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
#ax.set_zlabel('z')
#ax.legend(loc=2)
plt.show()
