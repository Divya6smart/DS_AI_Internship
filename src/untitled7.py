# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:08:06 2026

@author: divya
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,11]
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,4,3,2,1]
plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt

categories =['A','B','C']
values =[11,20,15]
plt.bar(categories,values)
plt.show()
