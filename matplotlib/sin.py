
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y = np.sin(x)

fig, axes = plt.subplots(figsize=(10,8),dpi=100)
axes.plot(x,y,'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('$y=\sin(x) ;graph$')
#input() #解决图像闪现的问题
#fig.show()
plt.show()
fig.savefig("../savefig/sin图像.png")
