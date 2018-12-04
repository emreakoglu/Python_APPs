# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:43:39 2018

@author: emreAkoglu
"""

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder,Imputer
import pandas as pd

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

# Buraya kadar  data_MergeCreate_DataFrame.py ile aynı zaten

# verileri 1/3 test verisi 2/3 eğitim verisi olarak bölüyoruz.Bu bölme işlemini random olarak yapıyoruz.
# bir sonraki derste cinsiyet tahmini yapılacağı için y sonuc_3(cinsiyet değerleri) dataframe'ine 
# x cinsiyet haricinde olan s(ülke, boy,kilo ve yas değerleri) dataframe'ine bağlıdır.
x_train, x_test,y_train,y_test = train_test_split(ulke_boy_kilo_yas,cinsiyet_DataFrame,test_size=0.33, random_state=0)
