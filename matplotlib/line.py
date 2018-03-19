import matplotlib.pyplot as plt
import matplotlib
import numpy as np

#解决中文乱码问题，引入Windows字体库

x = np.linspace(-8, 10, 50)
y = 2*x + 1
plt.plot(x,y)
plt.figure(1,figsize=(12,12))
#设置显示的轴数字
xticks = np.arange(-8,10,1)
plt.xticks(xticks)
yticks = np.arange(-8,10,1)
plt.yticks(yticks)
plt.xlabel(u'x')
plt.ylabel(u'y')
#挪动坐标轴
ax = plt.gca()
#去掉边框
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
#移位置，设为原点相交
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


x0 = 1
y0 =2*x0 + 1
plt.plot([x0,x0],[y0,0],'k--',linewidth=2 )
plt.scatter([x0,], [y0,], s=50, color='red')
#plt.title(u'Annotation 标注', fontproperties=myfont)
#标注方式1: 使用 annotate 接下来我们就对(x0, y0)这个点进行标注.
'''
其中参数xycoords='data' 是说基于数据的值来选位置, xytext=(+30, -30) 和
textcoords='offset points' 对于标注位置的描述 和 xy 偏差值, arrowprops是对图中箭头类型的一些设置.
'''
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0,y0), xycoords='data', xytext=(+30,-30),
             textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
'''
标注方式2: 使用 text
其中-3.7, 3,是选取text的位置, 空格需要用到转字符\ ,fontdict设置文本字体.
'''
plt.text(-1.2, 3, r'$.Annotation text . \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})
plt.savefig('../savefig/line.png')
plt.show()
