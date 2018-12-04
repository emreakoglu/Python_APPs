# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:34:50 2018

@author: emreAkoglu
"""

class A:
    renk = "Kırmızı"
    sekil = "Ucgen"
    


def scope_test():
    def do_local():
        spam = "local spam" # sadece do_local fonksiyonu içinde geçerlidir
        print("localden ", spam)

    def do_nonlocal():
        nonlocal spam# scope_test fonksiyonu içinde geçerlidir
        spam = "nonlocal spam"

    def do_global():
        global spam # bütün kodda geçerlidir.
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

    
def do_change(a):
    a.renk = "Mavi"
    a.sekil = "Kare"

a = A()

print(a.renk, a.sekil)

do_change(a)

print(a.renk, a.sekil)


