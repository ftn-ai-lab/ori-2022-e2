# -*- coding: utf-8 -*-
from __future__ import print_function

import numpy as np
from sklearn import linear_model

"""    
    @author: Bojan Blagojević  SW 9/2013
    
    Obrađeni podaci su poslužili za određivanje linearne zavisnosti broja
    vrsta životinja (na 42 britanska ostrva) u odnosu na sljedeće parametre:
        X1 - površina ostrva                (km2)
        X2 - nadmorska visina               (m)
        X3 - broj vrsta zemljišta
        X4 - geografska širina
        X5 - udaljenost od Velike Britanije (km)
        
    Dobijeni linearni model se može predstaviti sljedećom jednačinom:
        Y = 1.635e-04 * X1 + 1.001e-01 * X2 + 7.166e+01 * X3 - 7.379e+01 * X4 + 6.084e-01 * X5
    
    Zaključak koji slijedi iz formule je da površina ostrva najmanje utiče
    na broj vrsta koje žive na tom ostrvu, dok broj vrsta zemljišta i 
    geografska širina najviše utiču na dobijeni rezultat.
"""

def read_file(file_name):
    # Funkcija koja parsira fajl i vraća matricu prediktora i zavisnu promjenljivu y
    
    f = open(file_name, 'rb')
    
    # Parametri na osnovu kojih se pravi model
    area, elevation, num_of_soil_types, latitude, dist_from_britain = [],[],[],[],[]
    
    # Zavisna promjenljiva y
    num_of_species = []
    

    for line in f.readlines():
        params = line.split()
        area.append(float(params[1]))
        elevation.append(int(params[2]))
        num_of_soil_types.append(int(params[3]))
        latitude.append(float(params[4]))
        dist_from_britain.append(float(params[5]))
        num_of_species.append(int(params[6]))
        
    # Kreiranje matrice prediktora
    # Pošto numpy promjenljive area, elevation... tretira kao vrste,
    # matrica se mora transponovati
    x = np.array([area, elevation, num_of_soil_types, latitude, dist_from_britain]).transpose()
  
    return x, num_of_species
    

if __name__ == '__main__':
    # Čitanje iz fajla    
    x, y = read_file('britain_species.txt')
      
    lr = linear_model.LinearRegression()
    # Prosljeđivanje prediktora i zavisne promjenljive 
    lr.fit(x, y)
    
    # Ispisivanje dobijenih parametara
    print (lr.coef_)
    print (lr.intercept_)