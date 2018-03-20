#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure(1,figsize=(14,6))
ax1 = fig.add_subplot(1,2,1,projection='3d')
p1 = ax1.plot_surface(X,Y,Z, rstride=2,cstride=1,linewidth=0,
                      antialiased=False)

ax2 = fig.add_subplot(1,2,2,projection='3d')
p2 = ax2.plot_surface(X,Y,Z, rstride=1,cstride=1,linewidth=0,
                       cmap=cm.coolwarm,antialiased=False)
cb = fig.colorbar(p2,shrink=0.5)
fig.savefig('../savefig/plot_surface.png')


fig2 = plt.figure(2,figsize=(8,6))
ax3 = fig2.add_subplot(1,1,1,projection='3d')
p3 = ax3.plot_wireframe(X,Y,Z,rstride=2,cstride=1)
fig2.savefig('../savefig/plot_wireframe.png')


fig3 = plt.figure(3,figsize=(8,6))
ax4 = fig3.add_subplot(1,1,1,projection='3d')
ax4.plot_surface(X,Y,Z,cstride=1,rstride=1,alpha=0.25)
cset_z = ax4.contour(X,Y,Z,zdir='z',offset=-0.9, cmap=cm.coolwarm)
cset_x = ax4.contour(X,Y,Z,zdir='x',offset=-6.0, cmap=cm.coolwarm)
cset_y = ax4.contour(X,Y,Z,zdir='y',offset= 6.0, cmap=cm.coolwarm)

ax4.set_xlim3d(-2*np.pi,2*np.pi)
ax4.set_ylim3d(-2*np.pi,2*np.pi)
ax4.set_zlim3d(-2*np.pi,2*np.pi)
fig3.savefig('../savefig/plot_surface2.png')

fig4 = plt.figure(figsize=(12,6))
ax5 = fig4.add_subplot(1,2,1,projection='3d')
ax5.plot_surface(X,Y,Z,cstride=1,rstride=1,alpha=0.25)
ax5.view_init(30,45)
ax6 =fig4.add_subplot(1,2,2,projection='3d')
ax6.plot_wireframe(X,Y,Z,rstride=2,cstride=1)
ax6.view_init(70,30)
fig4.tight_layout()
fig4.savefig('../savefig/plot_wireframe2.png')
plt.show()




