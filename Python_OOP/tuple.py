# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:48:13 2018

@author: emreAkoglu
"""

l = [1,2,3]
t = (1,2,3) # tuple normal parantez ile oluşturulur, Immutable'dır, yani içeriği değiştirilemez
            # Immutable = Hafıza da bir kere oluşturulur ve daha değiştirilemez, ama yeniden oluşturulabilir

print(l)
print(t)

l[2] = 10
#t[2] = 10 #burda kod hata alacaktır

x,y,z = t # tuple unpack edilebilir, 1,2,3
print(x) # 1
print(z) # 3

z = 10 # z kendi başına 10 oldu, fakat tuple içindeki z değişmedi

print(t)

t = (x,y,z) # burda yeni bir tuple oluştuğu için z değeri artık 10 olacaktir, 
print(t) # (1,2,10)

v = ([1,2,3],[3,2,1]) # tuple içinde liste tutulabilir.
print(v)
v[0][1] = 100 # buradaki değişiklik listeye yapılıyor, tuple listeyi bir pointer ile tuttuğu için, aslında tuple üzerinde değişiklik yoktur

print(v)

t2 = 1,2,3 # tuple böyle de ifade edilebilir, bu da bir tuple'dır
print(t2)

