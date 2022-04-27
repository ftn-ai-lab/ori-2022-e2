"""
    @author:    SW 15/2013   Dragutin Marjanovic
    @email:     dmarjanovic94@gmail.com
"""

from __future__ import print_function


import csv # TODO use pandas
import codecs
import linreg_simple as lrs
import matplotlib.pyplot as plt

# Funkcija za citanje .csv fajla (comma separated file)
def read_csv_file(filepath, geotype = 'Long'):

    # Ako je geotype = "Long" tada je u pitanju geografska duzina
    # Ako je geotype = "Lat"  tada je u pitanju geografska sirina
    x = []
    # Stopa smrtnosti - Mort
    y = []

    index = 4 if geotype == "Long" else 1

    with open(filepath, 'rb') as f:
        # reader = csv.reader(f, delimiter=',')
        read = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter=',')
        for i,row in enumerate(read) :
            if i == 0: # skip header
                continue
            x.append(float(row[index]))
            y.append(int(row[2]))

    return x, y


# Funkcija da bismo mogli lakse pozvati i za geografsku duzinu i za geografsku sirinu
def linreg_cancer(geotype):
    x, y = read_csv_file('../../data/skincancer.csv', geotype)

    # Dobijamo koeficijente koristeci modul 'linreg_simple.py'
    slope, intercept = lrs.linear_regression(x, y)

    # Dobijamo regresionu pravu
    line_y = lrs.create_line(x, slope, intercept)

    # Crtamo grafik
    print("grafik")
    plt.plot(x, y, '.')
    plt.plot(x, line_y, 'r')
    plt.title('Slope: {0}, intercept: {1}'.format(slope, intercept))
    plt.show()

# TODO 3: implementirati primenu jednostavne linearne regresije
# nad podacima iz datoteke "data/skincancer.csv".
if __name__ == '__main__':
    # Pozivamo za geografsku sirinu
    linreg_cancer('Lat')

    # Pozivamo za geografsku duzinu
    linreg_cancer('Long')
