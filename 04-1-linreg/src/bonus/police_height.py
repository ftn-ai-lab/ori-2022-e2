# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:56:08 2016

@author: Sebastijan Stevanovic      SW 18/2013

    Uradjen je zadatak u kome procenjujemo koliko       
        sitting height (sedeca visina)
        upper arm (nadlaktica)
        forearm (podlaktica)
        hand (saka)
        upper leg (natkolenica)
        lower leg (potkolenica)
        foot  (stopalo)
        100*(forearm/upper arm) 
        100*(lower leg/upper leg)
    uticu na standing height (stojeca visina) zenskih aplikanata za policijsku akademiju.
    
    Iz dobijenih rezultata mozemo zakljuciti da "100*(lower leg/upper leg) = -0.5117723" najmanje utice,
    a "lower leg = 2.29053132" najvise utice na stojecu visinu (standing height).
    
"""

from __future__ import print_function

from sklearn import linear_model
import csv

if __name__ == '__main__':
    standing_height = []
    x = []
    with open('police_height.csv','rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            standing_height.append(float(row[1]))
            x.append([float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]),
                      float(row[7]), float(row[8]), float(row[9]), float(row[10])])
                   
    regression = linear_model.LinearRegression()
    regression.fit(x, standing_height)
    
    print('Coefficients: \n', regression.coef_)
    
    print('Intercept: \n', regression.intercept_)
    
                      