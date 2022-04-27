# -*- coding: utf-8 -*-
"""
@author: Stefan Kalnak     SW 10/2013

Brain weight (grams) and head size (cubic cm) for 237
adults classified by gender and age group.

Kolone: 
Pol (1 = muski, 2 = zenski)
Godine po grupama ( 1=20-46, 2=46+ )
Zapremina glave (cm^3)
Tezina mozga (u gramima)

Zakljucak: 
koeficijenti korelacije -22.5432537 (pol) , -23.96844543 (godine),   0.24421175 (zapr. glave)
Prema rezultatima najvise uticaja imaju pol i godine. Osobe muskog pola su imale vecu
tezinu mozga, kao i osobe koje pripadaju prvoj starosnoj grupi.
Najmanje uticaja je imala zapremina glave.

"""
import numpy as np
from sklearn import datasets, linear_model
import csv

if __name__ == '__main__':
    gender = []
    age = []
    head = []
    brain = []
    x = []
    with open('brain.csv','rb') as csvfile:
        podaci = csv.reader(csvfile, delimiter = ',')
        for row in podaci:
            gender.append(int(row[0]))
            age.append(int(row[1]))
            head.append(int(row[2]))
            brain.append(int(row[3]))
            x.append([int(row[0]), int(row[1]), int(row[2])])
    regression = linear_model.LinearRegression()
    regression.fit(x, brain)
    print('Coefficients: \n', regression.coef_)