# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:26:04 2018

@author: emreAkoglu
"""
# matrix de deniliyor


l = [1,2,3]

m = [[1,2,3,4],[3,4,5],l] # bu l liste elemanı shadow copy olarak geliyor, yani pointer olarak tutuluyor, l değişirse m'nin içindeki  l'de değişimiş olacaktır

print(m)
# l[1] = 100 # l'nin içeriği değişti, m'de bu değişiklikten etkilendi
print(m)

mt =  [[row[i] for row in m] for i in range(3)] # matrisin transpozunu alıyor, önce dıştaki döngü compile ediliyor


print(mt)

del(m[1]) # listenin 1. elemanını sil
print(m)