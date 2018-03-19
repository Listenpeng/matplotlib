#Author: Listen
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.DataFrame({'Height':[175,165,162,158,180],
                      'Age':[23,30,27,21,35],
                      'Scores':[80,100,70,85,65]},
                     index=['Jack','Leo','James','Lily','David'])
df.plot(kind='bar')
plt.savefig('../savefig/mylt_bar.png')
plt.show()



