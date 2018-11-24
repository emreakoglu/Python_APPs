# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:20:01 2018

@author: emreAkoglu
"""

l = []

for x in range(1,11): # x değişkeni sanki yukarda taanımlanmış gibi aşağıda da kullanılabilir
    l.append(x**2)

print(l)
print(x) # for içindeki x değişkeni artık tanımlıdır ve kullanılabilir

def f(x):
    return x+5

l2 = [2,8,3]
print(list(map(f,l2))) # map = f fonksiyon parametresine, l2 listesindeki elamanları teker teker çalıştır,
                       # çıkan sonucu list fonksiyonu ile tekrar listeye çevir
                       
print(list(map(lambda x:x+5,l2))) # lambda operaterü : isimsiz fonksiyon tanımlamak için kullanılır.
                                  # burada inline statement olarak x parametreli bir fonksiyon oluşturuluyor
                                  # ve x'in karaesi return değeri oluyor, bunu map ile kullanırsak, range(1,11)
                                  # sayesinde 1 den 11 kadar olan sayılar için, karelerini döndüren fonksiyon yazmış oluruz
                                  # işlem sona erdiğinde aslında böyle bir fonksiyon hiç varolmamış oluyor.
                                  # burada işlem bittiğinde x değişkenini de ortadan kaldırıyor

                       

squers = list(map(lambda x: x**2, range(1,11))) 
                                                
print(squers)

l3 = [z**2 for z in range(10)] # z**2 için 0'dan 10'a kadar olan z sayılarını kullan ve l3 listesine ata
                                # for içinde tanımlanan z değişkeni kullanılabilir.
print(l3)

l4 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y] # iç içe for döngüsü, if koşulu sağlandığı sürece, (x,y) ikililerini l4 listesine ekleeyecek

print (l4) #    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

l5 = [(x,y,z) for x in [1,2,3] for y,z in [(1,2),(2,3),(3,4)] if x!=y]
print (l5)