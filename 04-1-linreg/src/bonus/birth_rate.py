# -*- coding: utf-8 -*-
"""
@author:    Stefan Ristanović      SW3/2013
@email:     st.keky@gmail.com

 - Description: 
     Birth Rates, 
     per capita income, 
     proportion (ratio?) of population in farming, 
     and infant mortality
     during early 1950s for 30 nations.

 - Conclusion:
     In that period of time, the biggest impact on birth rate had the
     proportion of population in farming which is excpected result knowing
     history of that time. Slightly less influence had infant mortality, and
     per capita income had almost none of the impact (which is, one could say, 
     a surprising result knowing nowadays situation).
     
"""
from __future__ import print_function
import csv
from sklearn import linear_model
import numpy

def read_csv(file_name):
    with open(file_name) as csvfile:
        birth_rate, per_cap_inc, prop_on_farms, infant_mort = [], [], [], []
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            birth_rate.append(float(row[1]))
            per_cap_inc.append(float(row[2]))
            prop_on_farms.append(float(row[3]))
            infant_mort.append(float(row[4]))
            
        # create and transpose numpy array
        x = numpy.array([per_cap_inc, prop_on_farms, infant_mort]).transpose()
    return x, birth_rate
    
if __name__ == '__main__':
    # read data from dataset
    x, y = read_csv('birth_rate.csv');
    
    lm = linear_model.LinearRegression()
    lm.fit (x, y)
    
    print(lm.coef_)
    print(lm.intercept_)