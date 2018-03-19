#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x=np.array([x for x in range(1,6)])
k1=x**2
k2=x**3
k3=x**4
plt.figure()fi
plt.plot(x,k1,'-o')
plt.plot(x,k2,'-o')
plt.plot(x,k3,'-o')

ax=plt.gca()
ax.fill_between(x,0,k1,color='g',alpha=0.5)
ax.fill_between(x,k1,k2,color='y',alpha=0.5)
ax.fill_between(x,k2,k3,color='b',alpha=0.5)
plt.yticks([y for y in range(0,700,50)])
plt.legend(['y=x^2','y=x^3','y=x^4'],loc=2)
plt.savefig('../savefig/fill_between.png')
plt.show()
