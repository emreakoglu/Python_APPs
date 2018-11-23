# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:39:00 2018

@author: emreAkoglu
"""

from collections import deque

l = [44,55,66]
l.append(77)
print(l)
print(l.pop(0))  # 0 indexdeki elamanı pop et

l2 = deque([11,23,45])  # queue objelerinin python tarafında tanımlanması
print(l2)
l2.append(67)  
print(l2.popleft())  # listenin en başındaki elemanı alır
print(l2)