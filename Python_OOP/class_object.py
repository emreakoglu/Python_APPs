# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:10:32 2018

@author: emreAkoglu
"""

class araba:
    hiz = 0
    renk = ""
    tekersayisi = 4
    
    def hizlan(self):
        self.hiz = self.hiz + 1
        
x = araba()
x.hiz = 100
x.hizlan()

print ("arabanin hizi", x.hiz)

y = araba()
y.hiz = 70
y.hizlan()

print ("x arabanin hizi", x.hiz)
print ("y arabanin hizi", y.hiz)
