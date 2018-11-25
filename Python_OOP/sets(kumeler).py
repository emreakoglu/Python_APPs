# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:02:45 2018

@author: emreAkoglu
"""

l = [1,2,3] # liste - elemanların hangi sırada olduğu önemlidir
t = (1,2,3) # tuple - Değiştirelemdiği için kullanılır (Immutable)
k = {1,2,3} # kume / set - Elemanların sırası önemli değil, kümede olup olmaması önemli, bir eleman birden fazla kez olamaz

print(l)
print(t)
print(k)

k = {1,2,3,1,2,1,3} # böyle tanımlansa bile tekrarlılar atılarak oluşturulur

print(k)

k2 = set(l) # listeyi kümeye çevirebiliriz.

k3 = set('emreakoglu') # her bir karakter küme elemanıdır, tekrarlanan karakterler kümeden atılır, sırasız olarak oluşturuldu
k4 = set('bilgisayarkavramlari')

print(k3)
print(k4)

print(k3|k4) # kumelerin birleşim özelliği
print(k3&k4) # kumelerin kesişim özelliği
print(k3-k4) # kumelerin farkını alır
print(k3^k4) # bir kumede olup diğerinde olmayan (exclusive or, özel veya), (k3|k4) - (k3&k4)
print ((k3|k4) - (k3&k4))

