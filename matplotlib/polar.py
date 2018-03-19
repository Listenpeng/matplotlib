#!/usr/bin/ env python3
#coding = utf-8
import matplotlib.pyplot as plt
import numpy as np

#主要使用plt选择对象

#定义函数
x = np.linspace(-10*np.pi,10*np.pi,1000 )
r = 2-2*np.sin(5*x )

#定义画布，绘制图像,polar指定极坐标
ax1 = plt.subplot(projection='polar')
ax1.plot(x,r,label=u'flower',color='red', linewidth=1)

#显示图例
plt.legend(loc=3)

#设置图表标题
plt.title(u'$r=2-2\sin(5x)$')
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.savefig('../savefig/polar.png')
plt.show()
