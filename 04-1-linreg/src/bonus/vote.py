# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:55:23 2016

@author: Nemanja Zunic sw63/2014
Dataset:  clinton1.dat
Source: U.S. Census Bureau
Procenat glasova za Bila Klintona 1992. po saveznim drzavama 
i demografskim promenljivim

intercept: -35.2922086912
za demografske podatke sam koristio:
    1. procenat siromasnih            - coef:  0.727701 
    2. procenat veterana              - coef:  0.13557432
    3. procenat osoba zenskog pola    - coef:  1.20880104

koeficijenti su svi pozitivni tako da se moze zakljuciti da su ove 
grupe glasaca povoljno uticale na izborni rezultat, posebno zenska populacija

Bil je pobedio sa 43% glasova tako da jednacina izgleda
43 ~  -35.292 + 0.727 * x1 + 0.135 * x2 + 1.208 * x3

"""
from __future__ import print_function
from sklearn import linear_model

def read_file(filepath):

    percent_votes = []
    X = [] #procenat siromasnih, procenat veterana,  procenat osoba zenskog pola
    
    file = open(filepath, 'r')
    content = file.readlines()
    for row in content:
        percent_votes.append(float(row.split(',')[1]))
        X.append([float(row.split(',')[5]), float(row.split(',')[6]), float(row.split(',')[7])])

    return X, percent_votes
        
def create_line(x, slope, intercept):
    y = [predict(xx, slope, intercept) for xx in x]
    return y
    
    
def predict(x, b, a):
    return a + b*x       
    
if __name__ == '__main__':
    
    X, percent_votes = read_file("vote.csv")
    lm = linear_model.LinearRegression()
    lm.fit(X, percent_votes)
    print(lm.coef_)
    print(lm.intercept_)
