from __future__ import print_function
from sklearn import linear_model

"""
    @author:    Milorad Vojnović SW12/2013
    
    Ispitivano je koliko određeni parametri utiču na cenu kuće.
    
    Parametri su: 
        1. Cene lokalnih kuća (u hiljadama dolara)
        2. Broj kupatila
        3. Površina celokupnog objekta u hiljadama kvadratnih funti
        4. Površina dnevnog boravka u hiljadama kvadratnih funti
        5. Broj garaža
        6. Broj soba
        7. Broj spavaćih soba
        8. Starost objekta
        9. Materijal: 1 = cigla, 2 = cigla/drvo, 3 = aluminum/drvo, 4 = drvo
        10. Tip kuće: 1 = two story, 2 = split level, 3 = ranch
        11. Broj kamina
        
    Dobijena jednačina: 
        y = 2.54245910924 + 0.84203461 * x1 + 9.13727309 * x2 + 0.1805502 * x3 + 
        + 13.31511517 * x4 + 1.93053047 * x5 + (-1.07030169) * x6 + 
        (-0.30201195) * x7 + (-0.07198748) * x8 + 1.02264378 * x9 + 
        + 1.33991086 * x10 + 2.78686263 * x11
        
    Iz ovoga možemo zaključiti da na cenu kuće najviše utiču parametri pod 2 i 4,
    a najmanje utiču parametri pod 3, 7, 8.
"""

if __name__ == '__main__':
    with open('selling_prices.txt') as file:
        y, x = [], []
        for row in file.readlines():
            temp = []
            row = row.split()
            y.append(float(row[12]))
            for value in row:
                temp.append(float(value))
                
            del temp[0]#izbacujemo redni broj kuće u fajlu
            del temp[11]#izbacujemo cenu kuće
            x.append(temp)

    lm = linear_model.LinearRegression()
    # Prosleđujemo prediktora x i zavisnu promenljivu y
    lm.fit (x, y)

    # Stampamo koeficijente i intercept
    print (lm.coef_)
    print (lm.intercept_)
