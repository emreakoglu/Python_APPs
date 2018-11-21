# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:18:27 2018

@author: emreAkoglu
"""

def f(x):
    return x+10

print(f(8))

def fib(n):
    a,b = 0,1
    while a<n:
        print(a)
        a,b=b,a+b
        
fib(20)

def fact(n):
    sonuc = 1
    a = 1
    while a<=n:
        sonuc = sonuc * a
        a = a+1
    
    return sonuc

print(fact(5))


# recursive fact

def fact_recursive (n):
    if (n!=0):
        return n*fact_recursive(n-1)
    else:
        return 1
    
print(fact_recursive(5))

# recursive fib
a = 0
def fib_recursive(n):
    
    if (n==0): return 0
    if (n==1): return 1
    return fib_recursive(n-2) + fib_recursive(n-1)

print (fib_recursive(7))

def default_Param(x,y=3):
    return x + y

print (default_Param(5,10))
print(default_Param(5))
    
    

        