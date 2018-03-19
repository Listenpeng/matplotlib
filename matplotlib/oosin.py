#encoding = utf-8
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 *np.pi * t)

#面向对象绘图
#生成画布、图幅
fig, ax = plt.subplots()
ax.plot(t, s)
#设置其它
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
#设置次刻度线
ax.grid()
#保存图片
fig.savefig('../savefig/oosin.png')
plt.show()
plt.close()
