# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:46:59 2018

@author: emreAkoglu
"""

knights_dict = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights_dict.items():
    print(k,v)

# enumerate : bir değişkenin alacağı değerleri kısıtlamak için kullanılır. Mesela: güneş sistemindeki gezegenlerin adları
    
for i,v in enumerate(['merkür','venüs','dünya','mars','jüpiter','satürn','uranüs','neptün']):
    print(i,v)      # elemanları 0. indexten başlayarak (index) (değer) şeklinde yazdıracak
    
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
    
