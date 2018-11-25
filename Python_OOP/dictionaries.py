# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:20:12 2018

@author: emreAkoglu
"""

# key-value ikisi olarak tutulur

tel = {'jack': 4098, 'sape': 4139}
print(tel['jack'])

d_liste = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # tuplelardan oluşan liste, sözlüğe çevrildi

print(type([('sape', 4139), ('guido', 4127), ('jack', 4098)])) # değişkenin türünün ne olduğunu anlamak için

t = (['emre',1],['ahmet',2])
print(t)

d_tuple = dict(t) #  listelerden oluşan tuple, sözlüğe çevrildi

print(d_tuple)