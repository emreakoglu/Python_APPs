# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:41:19 2018

@author: emreAkoglu
"""


#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('eksikveriler.csv')

ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn.preprocessing import LabelEncoder ,OneHotEncoder

le = LabelEncoder() # Değerleri bir sayıya çeviriyor, her değeri bir sayıya çeviriyor

ulke[:,0] = le.fit_transform(ulke[:,0])

print(ulke)

#from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all') # Her başlık altına denk gelen sayıyı 1 yaparak çeviriyor

ulke = ohe.fit_transform(ulke).toarray()

print (ulke)