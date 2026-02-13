# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:03:20 2026

@author: divya
"""

import pandas as pd

s1 = pd.Series([50,20,60,90])
s2 = pd.Series([50,20,60],index = ['a','b','c'])

print(s1)
print(s2)

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)