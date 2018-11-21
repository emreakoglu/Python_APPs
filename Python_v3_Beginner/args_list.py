# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:06:26 2018

@author: emreAkoglu
"""
# args_list

def sum_list(*a):
    total = 0
    for i in a:
        total = total + i
        
    return total

print(sum_list(1,2,3,4))


def sum_list_first(first,*a):
    total = first
    print("first:" + str(first))
    for i in a:
        total = total + i
    return total

print(sum_list_first(2,3,4,5))


def sum_list_dictionary(**a):
    for i in a:
        print(str(i) + str(a[i]))
        
sum_list_dictionary(a=2,b=3,c=4)