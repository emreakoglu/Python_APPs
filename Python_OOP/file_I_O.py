# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:16:25 2018

@author: emreAkoglu
"""
import json

f = open('bilgisayar.txt','w') # ilk parametre dosya ismi, ikinci parametre modudur, w: write , r:read
f.write('File writing with Python v3')
f.close() # close yapmadan, dosyaya yazma işlemi yapılmaz

f = open('bilgisayar.txt','r')
print(f.read())
f.close()

f = open('bilgisayar.txt','r')

for line in f:
    print(line)
    
    
json_sample = json.dumps([1,'simple','list'])

print(json_sample)

    