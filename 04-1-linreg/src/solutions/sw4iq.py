# author: Aleksandar Novakovic SW 4/2013

from __future__ import print_function

from sklearn.linear_model import LinearRegression

# TODO 4: implementirati primenu visestruke linearne regresije
# nad podacima iz datoteke "data/iq.tsv".
# Korisiti implementaciju linearne regresije u alatu scikit-learn

# Regression results show that brain volume and person's height have influence on IQ,
# while person's weight doesn't.

if __name__ == '__main__':
    data_x = []
    data_y = []
    with open('./../../data/iq.tsv', 'r') as file:
        for line in file:
            try:
                row = [float(num) for num in line.split()]
                data_x.append(row[1:])
                data_y.append(row[0])
            except:
                pass
    lr = LinearRegression().fit(data_x, data_y)
    print(lr.coef_)
    print(lr.intercept_)