# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:22:05 2018

@author: emreAkoglu
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('eksikveriler.csv')

print (veriler)

#boy = veriler[['boy']]
#print (boy)

#boykilo = veriler[['boy','kilo']]
#print(boykilo)

#class insan():
#    boy = 180
#    def kosmak(self,b):
#        return b+10
#    
#ali = insan()
#print(ali.boy)
#print(ali.kosmak(90))
#
#l = [1,2,3] # liste
#print(l.pop(1))

#sci-kit learn
from sklearn.preprocessing import Imputer

imputer  =  Imputer(missing_values='NaN',strategy='mean',axis=0)

Yas = veriler.iloc[:,1:4].values
print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])

print (Yas)
