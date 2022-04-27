"""
    @author:    SW 15/2013   Dragutin Marjanovic
    @email:     dmarjanovic94@gmail.com

    Zadatak koji je obradjen je zavisnost cijene po ton-mile avioprevoza od 7 parametara.
    Ti parametri su:
        - duzina leta
        - brzina aviona (mph)
        - vrijeme leta
        - ukupan broj usluzenih putnika
        - opterecenje po ton-mile
        - raspolozive tone po vazduhoplovnoj milji
        - prihodi firme

    Zakljucak do kog se doslo je postoji odstupanja od pravih vrijednosti.
    Dobijenim koeficijentima zakljucujemo da 'ukupan broj usluzenih putnika'
    najmanje utice (koef. 3*10^-3). Isto tako, 'brzina aviona' i 'prihodi firme'
    malo uticu na dobijenu vrijednost (reda 10^-1).
"""

from __future__ import print_function

import csv
from sklearn import linear_model


# Funkcija za formiranje matrice prediktora
# U nasem slucaju imamo 7 prediktora (parametri navedeni gore)
def form_predictors(X1, X2, X3, X4, X5, X6, X7):
    X = []
    for x1, x2, x3, x4, x5, x6, x7 in zip(X1, X2, X3, X4, X5, X6, X7):
        X.append([x1, x2, x3, x4, x5, x6, x7])

    return X

# Funkcija za citanje .csv fajla
def read_csv_file(filepath):

    # Parametri
    flight_len, plane_speed, flight_time, population_served = [], [], [], []
    load_factor, available_tons_pam, firms_assets = [], [], []

    # Zavisna promjenljiva 'y'
    total_operating_cost = []

    with open(filepath, 'rb') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            flight_len.append(int(row[1]))
            plane_speed.append(int(row[2]))
            flight_time.append(float(row[3]))
            population_served.append(int(row[4]))
            load_factor.append(float(row[7]))
            available_tons_pam.append(float(row[8]))
            firms_assets.append(float(row[9]))

            total_operating_cost.append(float(row[5]))


    X = form_predictors(flight_len, plane_speed, flight_time, population_served,
                        load_factor, available_tons_pam, firms_assets)

    return X, total_operating_cost

if __name__ == '__main__':

    # Ucitamo .csv fajl
    X, y = read_csv_file('airline_costs.csv')

    lm = linear_model.LinearRegression()
    # Prosljedjujemo prediktore (X) i zavisnu promjenljivu (y)
    lm.fit (X, y)

    # Stampamo koeficijente
    print (lm.coef_)
    # Stampamo 'intercept'
    print (lm.intercept_)

    # Prvi red parametara. Prava vrijednost 116.3. Dobijena vrijednost 157.27.
    print (lm.predict([[57, 133, 6.1, 20200, 0.4, 2.4, 21.13]]))
    # Drugi red parametara. Prava vrijednost 43. Dobijena vrijednost 25.19.
    print (lm.predict([[270, 216, 6.93, 56928, 0.689, 5.776, 1436.53]]))
    # Treci red parametara. Prava vrijednost 141.5. Dobijena vrijednost 249.95.
    print (lm.predict([[100, 140, 4.45, 183, 0.358, 2.207, 6.65]]))
