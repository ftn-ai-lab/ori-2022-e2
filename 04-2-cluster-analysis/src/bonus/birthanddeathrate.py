# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:26:28 2016

@author: Milorad Vojnović SW12/2013

Za izradu su korišćene scikit-learn biblioteke.

Zadatak: Izvršiti klasteriraziju podataka koji predstavljaju stopu
stopu rodnosti i smrtnosti ljudi po 1000 stanovnika. Korišćeni su podaci od
70 država iz 1966.

Kod K-meansa prvom klasteru pripadaju države koje imaju stopu rodnosti
manju od 30, drugom klasteru sa stopom rodnosti od 30-50, a trećem države sa
stopom rodnosti većom od 50 i stopom smrtnosti većom od 20.

Kod DB-scana su stvorena dva klastera. U prvom države sa stopom rodnosti do 30,
drugom od 30-50. S obzirom da je minimalni broj država za kreiranje klastera 5,
u podacima se nalazi 3 države koje se ne nalaze ni u jednom klasteru. To su 
Danska koja je jedina država sa stopom smrtnosti većom od stope rodnosti, 
zatim Gana i Obala Slonovače koje imaju više od 50 stopu rodnosti i stopu
smrtnosti veću od 20.
"""

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

data_list = []
countries = []

with open('birthanddeathrate.txt','r') as f:
    for row in f:
        data  = row.split();
        countries.append(data[0])
        data = data[1:]
        data = [float(i) for i in data]
        data_list.append(data)
   
data_array = np.array(data_list)
y_pred_km = KMeans(n_clusters=3).fit_predict(data_array)
y_pred_db = DBSCAN(eps=4).fit_predict(data_array)

plt.figure(figsize=(12, 12))
plt.subplot(224)
plt.scatter(data_array[:, 0], data_array[:, 1], c=y_pred_km)
plt.title("K-Means")
plt.xlabel('Birth rate')
plt.ylabel('Death rate')
plt.show()

plt.figure(figsize=(12, 12))
plt.subplot(224)
plt.scatter(data_array[:, 0], data_array[:, 1], c=y_pred_db)
plt.title("DB Scan")
plt.xlabel('Birth rate')
plt.ylabel('Death rate')
plt.show()

