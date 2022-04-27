# -*- coding: utf-8 -*-
"""
Spyder Editor

    @Author: Jelena Banjac SW 16/2013 <jelena.b94@gmail.com>
    -----------------------------------------------------------------------------------
    Efficiency of Muscular Work
    -----------------------------------------------------------------------------------
    QUESTION: How do Body Mass and Work Levels impact 
              on Heat Production (losing calories)?    
    
    Dataset description:
        Dataset: muscular_work.dat
    
        Source: M. Greenwood (1918). "On the Efficiency of Muscular Work,"
        Proceedings of the Royal Society of London, Series B, Containing Papers
        of a Biological Character, Vol.90, #627, pp.199-214
        (Originally from Jules Amar (1910), 'Le Rendement de la Machine Humaine')
        
        Description: Measurements of Heat Production (calories) at various
        Body Masses (kgs) and Work levels (Calories/hour) on a stationary bike.
          
        Note original observation for Case 19 (Heat Output) is clearly a typo
        in original paper and has been changed from 3936 to 2936 (which makes
        all calculations in agreement with authors)
    
    Problem description:
        Models Considered:
          NOW -> (i)   E(H) = a0 + a1 * M + a2 * W (muscles_lin_reg1.py)
                (ii)  E(H) = b0 + b1 * M + ( W / ( b3 + b4 * M ) ) (muscles_lin_reg2.py)
        
        Variables/Columns
        B - Body Mass (kgs)  5-8
        W - Work Level (calories)    12-16
        H - Heat Output (calories/hour)   21-24
    
    Conclusion:
        --- Coefficients --- (Better way to solve this problem)
        Formula used: E(H) = a0 + a1 * M + a2 * W
        Final formula: E(H) = 977.42 + 17.78 * M + 6.24 * W
        
        Conclusion based on final formula is that the Body Mass (kgs)
        has the gratest impact on Heat Production(calories). The smallest impact
        has Work Level (calories/hour), however, that impact is not negligible.
        
        --- 3D Graph ---
        Features Body Masses (kgs) and Work levels (Calories/hour) of the 
        muscles-dataset are fitted and plotted below. 
        It illustrates that although Body Masses have a strong coefficient on the 
        full model, it does not give us much regarding y when compared 
        to just Work Level.
        
        --- Why finding coefficients are better this way? ---
        In this case (Linear Regression) concluding something from 3D graph in 
        not very reliable. Finding coefficients is much more accurate.
        However, 3D Graph is more reliable in the Least Squares method for solving.
        Solution of that problem is in muscular_work.py file.

"""
from __future__ import print_function
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt

print(__doc__)

body_mass, work_level  = [], []  
heat_output = []

# Read data from .dat file
def read_dat_file(file_path):
    file = open(file_path,"r") 
    lines = file.readlines() 
    file.close() 
    for line in lines:    
        body_mass.append(float(line.strip().split()[0]))
        work_level.append(float(line.strip().split()[1]))
        heat_output.append(float(line.strip().split()[2]))
   
    return np.array([body_mass, work_level]).T, heat_output

# Plot the figure
def plot_figs(fig_num, elev, azim, clf,a):
    fig = plt.figure(fig_num, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, elev=elev, azim=azim)

    ax.scatter(body_mass, work_level, heat_output, c='k', marker='+')
    
    X = np.arange(55, 85, 0.5)
    Y = np.arange(90, 180, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = a[0] + a[1]*X + a[2]*Y
    ax.plot_surface(X, Y, Z,alpha=.5, antialiased=True,rstride=200, cstride=100, cmap=plt.cm.coolwarm)
                 
    ax.set_xlabel('BODY_MASS', color='b')
    ax.set_ylabel('WORK_LEVEL', color='b')
    ax.set_zlabel('HEAT_OUTPUT', color='b')
    
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    
    ax.zaxis.set_major_locator(plt.LinearLocator(10))
    ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.f'))
    ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.f'))
    ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.f'))
    

if __name__ == '__main__':
    x, y = read_dat_file('muscular_work.dat')
    
    # Ordinary least squares Linear Regression
    lin_reg = linear_model.LinearRegression()
    
    # Fit linear model
    lin_reg.fit(x, y)
    
    # Estimated coefficients for the linear regression problem
    print ('Coefficients: ',lin_reg.coef_)
    # Independent term in the linear model
    print ('Independent term: ',lin_reg.intercept_)
    
    # Generate the three different figures from different views
    a = [lin_reg.intercept_,lin_reg.coef_[0], lin_reg.coef_[1] ]    
    elev = 43.5
    azim = -110
    plot_figs(1, elev, azim, lin_reg,a)
    plt.title('(1) Linear regression', color='g')
    
    elev = -.5
    azim = 0
    plot_figs(2, elev, azim, lin_reg,a)
    plt.title('(2) Linear regression', loc='left', color='g')
    
    elev = -.5
    azim = 90
    plot_figs(3, elev, azim, lin_reg,a)
    plt.title('(3) Linear regression', loc='right', color='g')
    
    plt.show()
