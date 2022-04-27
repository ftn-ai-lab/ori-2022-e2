# -*-
# author: Aleksandar Novakovic (SW 4/2013)
# relating air pollution to mortality using regression

from __future__ import print_function

from sklearn.linear_model import LinearRegression

# Cols:
# A1 average annual precipitation in inches
# A2 average January temperature in degrees Fahrenheit
# A3 average July temperature in degrees Fahrenheit
# A4 percent of 1960 SMSA population 65 years old or older
# A5 household size, 1960
# A6 schooling for persons over 22
# A7 household with full kitchens
# A8 population per square mile in urbanized areas
# A9 percent nonwhite population
# A10 percent office workers
# A11 poor families (annual income under $3000)
# A12 relative pollution potential of hydrocarbons
# A13 relative pollution potential of oxides of Nitrogen
# A14 relative pollution of Sulfur Dioxide
# A15 percent relative humidity, annual average at 1pm.
# B   the death rate.

# from given results we can see that household size has the most influence on mortality
# least influental are population per square mile in urbanized areas and relative pollution
# of Sulfur Dioxide

if __name__ == '__main__':
    data_x = []
    data_y = []
    with open('air_pollution_mortality.tsv', 'r') as file:
        for line in file:
            data = [float(num) for num in line.split()]
            data_x.append(data[:-1])
            data_y.append(data[-1])
    lr = LinearRegression().fit(data_x, data_y)
    print(lr.coef_)
    print(lr.intercept_)
