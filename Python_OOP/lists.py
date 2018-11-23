# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:56:46 2018

@author: emreAkoglu
"""

l=[1,2,3,4]
print(l)
l.append(55)
print(l)
l.insert(2,111) # insert metodunda birinci parametre verinin ekleneceği index
l.append(111) # her zaman sona ekleme yapar
print(l)

l.remove(111) # ilk bulduğu 111 elmanını kaldırdı
print(l)
print(l.pop()) # listeden elemanı da kaldırır
print(l)

print(l.index(55)) # 55 elemanının bulunduğu index

l.append(1)
l2=[3,4,2]
l.extend(l2) # listeye,yeni bir liste ekler, append bu noktada liste içinde liste olarak ekleyecekti

print(l.count(1)) # listede o elamandan kaç adet olduğunu kontrol eder

l.sort() # listeyi sıralı hale getirir, yani sıralanmış olarak listeyi düzenler
print(l)

l.clear()
print(l)

l3 = l2 # sığ kopyalama oldu, l3 hafıza da  (pointer) gibi olarak l2 yi gösteriyor.
l3.append(600) # aslında bellekte tek bir tane liste var, l2 ve l3 değişkenleri aynı listeyi referans ediyor.
print(l3)
print(l2)

l4 = l2.copy() # hafızada bir tane daha bu listeden kopya oluşturuldu
l4.append(700) # sadece l4' e append edildi

print(l2)
print(l4)


