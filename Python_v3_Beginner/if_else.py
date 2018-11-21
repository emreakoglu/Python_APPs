# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:24:55 2018

@author: emreAkoglu
"""

x = int(input("bir sayı giriniz"))
if x < 100:
    print("less number")
    x=500
elif x>500:
    print ("great number")
else:
    print("in between250")
    
print("x'in yeni degeri" + str(x))