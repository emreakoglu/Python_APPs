# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:02:20 2018

@author: emreAkoglu
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder,Imputer

veriler = pd.read_csv('eksikveriler.csv')

imputer  =  Imputer(missing_values='NaN',strategy='mean',axis=0)

Yas = veriler.iloc[:,1:4].values

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])

ulke = veriler.iloc[:,0:1].values

le = LabelEncoder() # Değerleri bir sayıya çeviriyor, her değeri bir sayıya çeviriyor

ulke[:,0] = le.fit_transform(ulke[:,0])

ohe = OneHotEncoder(categorical_features='all') # Her başlık altına denk gelen sayıyı 1 yaparak çeviriyor

ulke = ohe.fit_transform(ulke).toarray()

sonuc_Ulke = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])

boy_kilo_yas = pd.DataFrame(data = Yas, index = range(22), columns = ['boy','kilo','yas']) 

cinsiyet = veriler.iloc[:,-1].values

print(cinsiyet)

cinsiyet_DataFrame = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])

ulke_boy_kilo_yas = pd.concat([sonuc_Ulke, boy_kilo_yas],axis = 1)

ulke_boy_kilo_yas_cinsiyet = pd.concat([ulke_boy_kilo_yas,cinsiyet_DataFrame],axis = 1)