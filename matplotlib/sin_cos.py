#coding= utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y = np.sin(x)
z = np.cos(x)

#fig, ax = plt.subplot(1,2,1)
ax = plt.figure(figsize=(8,4), dpi=100)
plt.plot(x,y, label='$y=sin(x)$',color='red', linewidth=1)
plt.plot(x,z, '--',label='$y=cos(x)$', color='blue')
#显示图例
plt.legend(loc=1)
#设置绘图轴的区间
plt.xlim(-11,11,1.0)
plt.ylim(-1.5,1.5)

#设置x\y轴的标签
plt.xlabel('x')
plt.ylabel('y')
import matplotlib
#设置坐标轴值的刻度字体大小
matplotlib.rc('xtick', labelsize=4)
matplotlib.rc('ytick', labelsize=4)

#特殊点的注释
t = 2*np.pi/3
t1= np.pi*2
y1= np.sin(t1)
plt.plot([t,t], [-1.5, np.cos(t)],'--',color='blue')#多画了一条直线
plt.scatter([t,], [np.cos(t),],50,color='blue')#这是画点
plt.annotate(r'$\cos(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(+10,-30),textcoords='offset points', fontsize=8,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.0'))
plt.plot([t1,t1], [y1,-1.5],5,'--',color='red')#这是画点
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t1, np.sin(t1)), xycoords='data',
             xytext=(+10,+30),textcoords='offset points', fontsize=8,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

#设置图表标题
plt.title(u'sinx-cosx graph')

#设置箭头
#plt.arrow(x,y, dx='.', dy='.')
plt.savefig('../savefig/sin_cos.png')
plt.show()
