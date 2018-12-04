# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:40:26 2018

@author: emreAkoglu
"""

import fibo # başka dosyayı import ettik
import sys

fibo.fib(5)

print(fibo.fib2(4))

print("dosya ismi : "+sys.argv[0]) # sys.argv[0] dosya ismidir(fibotest.py)
print(fibo.fib2(int(sys.argv[1]))) # consoledan verdiğin parametre, python fibotest.py 10
                                # Ayrıca argümanlar her zaman string okunur, int'e bizim çevirmemi gerekir