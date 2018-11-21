# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:37:54 2018

@author: emreAkoglu
"""

i= 1
while i<10:
    print(i)
    i=i+1
    
print ("end of while")

# fibonacci serisi
# 0,1,1,2,3,5,8,13,21

a,b = 0,1
while a < 22:
    print(a)
    c= a+b
    a = b
    b = c
    
    
# for loop
print ("for loop")
total = 0
l1= [1,2,39,5,3]
for i in l1:
    total = total+i
    print(i)
    
print(total)

for x in range(20):
    if (x%3==0):
        continue  # döngüye devam et
    elif (x%5==0):
        break  # döngüyü kırar
    print(x)
    
asallar = []
for x in range(2,100):
    for y in range(2,x):
        if(x%y==0):
            print(x,"asal sayı değildir")
            break
    else:
        asallar.append(x)
        print(x,"asal sayıdır")
        
print(asallar)
        
    

    
