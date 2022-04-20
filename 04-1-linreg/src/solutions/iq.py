"""
    @author:    SW 15/2013   Dragutin Marjanovic
    @email:     dmarjanovic94@gmail.com
"""

from __future__ import print_function


import csv
from sklearn import linear_model

# Funkcija za citanje .tsv fajla (tab separated file)
def read_tsv_file(filepath):

    piq, brain, height, weight = [], [], [], []

    with open(filepath, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader, None)  # Preskacemo header
        for row in reader:
            piq.append(int(row[0]))
            brain.append(float(row[1]))
            height.append(float(row[2]))
            weight.append(int(row[3]))

    return piq, brain, height, weight


# TODO 4: implementirati primenu visestruke linearne regresije
# nad podacima iz datoteke "data/iq.tsv".
# Korisiti implementaciju linearne regresije u alatu scikit-learn
if __name__ == '__main__':
    y, x1, x2, x3 = read_tsv_file('../../data/iq.tsv')

    # Kreiramo listu x vrijednosti. Ona treba da izlgeda:
    #   [81.69,	 64.5, 118]
    #   [103.84, 73.3, 143]
    #          ...

    X = [[i, j, k] for i, j, k in zip(x1, x2, x3)]

    lm = linear_model.LinearRegression()
    # Prosljedjujemo prediktore (X) i zavisnu promjenljivu (y)
    lm.fit (X, y)

    # Stampamo koeficijente gdje svaki odgovara redom proslijedjenim X parametrima
    """
        lm.coef_[0] - zavisnost od zapremine mozga
        lm.coef_[1] - zavisnost od visine
        lm.coef_[2] - zavisnost od tezine
    """
    print (lm.coef_)

    # Stampamo 'intercept'
    print (lm.intercept_)
