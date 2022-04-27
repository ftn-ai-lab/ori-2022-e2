# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:22:50 2016

@author: Arsenije Vladisavljev SW2/2013

Plant Diversity on Northeastern North American Islands
--------------------------------------------------------

Cols:
Total plant species richness   (tot.rich)
area in hectares    (area)
latitude in degrees North Lat (latitude)
elevation in meters above sea level  (elev)
distance from maimland in km  (dist.mnland) 
distance from nearest island in km   (dist.island)
years since isolation   (years.isol)
years since deglaciation    (years.deglac)
human population   (human.pop)
human population density per hectare  (human.dens)


SOLUTION
----------

Intercept value is -5928.49260117.

Coef. for:
    area in hectares is                         -0.0431918775
    latitude is                                 79.1401161
    elevation in meters above sea level is       2.41723533
    distance from maimland in km is             -1.40654929
    distance from nearest island in km is       15.9197082
    years since isolation is                     0.00836552726
    years since deglaciation is                  0.192716670
    human population  is                         0.0879383643
    human population density per hectare is     26.7425669

From given results we can see that latitude has the most influence on total plant
species richness.
Next is human population density per hectare, then distance from the nearest island.
Other factors do not have so much influence.
"""


from __future__ import print_function
import numpy as np
import csv
from sklearn.linear_model import LinearRegression

def read_file():
    tot_rich, area, latitude, dist_mnland, dist_island = [],[],[],[],[]
    years_isol, elev, years_deglac, human_pop, human_dens = [],[],[],[],[]
    
    with open('plant_diversity_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tot_rich.append(float(row["tot.rich"]))
            area.append(float(row["area"]))
            latitude.append(float(row["latitude"]))
            elev.append(float(row["elev"]))
            dist_mnland.append(float(row["dist.mnland"]))
            dist_island.append(float(row["dist.island"]))
            years_isol.append(float(row["years.isol"]))
            years_deglac.append(float(row["years.deglac"]))
            human_pop.append(float(row["human.pop"]))
            human_dens.append(float(row["human.dens"]))


    x = np.array([area, latitude, elev, 
                    dist_mnland, dist_island, years_isol, years_deglac,
                    human_pop, human_dens]).transpose()
  
    return x, tot_rich

if __name__ == '__main__':   
    x, y = read_file()
      
    lr = LinearRegression().fit(x, y)
    print(lr.coef_)
    print(lr.intercept_)