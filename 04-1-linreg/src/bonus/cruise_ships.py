# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 01:27:26 2016

@author: Dusan Borovcanin SW36/2013
"""

from __future__ import print_function
from sklearn.linear_model import LinearRegression
#Dataset desription:

#Measurements of ship size, capacity, crew, for 158 cruise
#ships.

#Variables/Columns
#Ship Name
#Company name
#Tonnage (1000s of tons)
#passengers (100s)
#Length (100s of feet)
#Cabins  (100s)
#Passenger Density
#Crew  (100s)
#-----------------------------------------------
# Calculated depndency between passenger cappacity and rest of the data.
# From results we can conclude that number of cabines and number of passengers
# are deeply connected, as we expected. Ship length and tonnage are, surprisingly, the
# least important. Crew size is very influential (unsurprisingly) and passenger
# density is much less (2.5 times) influential.


if __name__ == '__main__':
    x = [] #contains tonnage, length, cabins, pass. density and crew size
    y = []

    f = open("cruise_ship.txt", "r")

    for line in f.readlines():
        row = line.split()
        num_row = [float(item) for item in row[2:]]
        y.append(num_row[1]*100)
        del num_row[1]
        x.append(num_row)
        
    regression = LinearRegression().fit(x, y)
    print(regression.coef_)
    print(regression.intercept_)     
    
    
