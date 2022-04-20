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
                 (i)   E(H) = a0 + a1 * M + a2 * W (muscles_lin_reg1.py)
         NOW -> (ii)  E(H) = b0 + b1 * M + ( W / ( b3 + b4 * M ) ) (muscles_lin_reg2.py)
        
        Variables/Columns
        B - Body Mass (kgs)  5-8
        W - Work Level (calories)    12-16
        H - Heat Output (calories/hour)   21-24
    
    Conclusion:
        --- Coefficients ---
        Formula used: E(H) = b0 + b1 * M + ( W / ( b3 + b4 * M ) )
        Final formula: E(H) = 1.646e+03 + 1.983e+01 * M + ( W / ( 2.262e+07 - 1.320e+05 * M ) )
        
        Concluding something from this final formula is much harder than it was 
        with linear regression. Equation is not linear. It is much easier to
        conclude from the Graph.
        
        --- 3D Graph --- (Better way to solve this problem)
        Features Body Masses (kgs) and Work levels (Calories/hour) of the 
        muscles-dataset are fitted and plotted below. 
        It illustrates that Body Masses have a strong impact on Heat Production
        (because estimated plane and heat_output-work_level plane have smaller 
        inclination angle). On the other hand, impact of Woking Level is almost
        negligible (because estimated plane and heat_output-body_mass plane
        have inclination angle about 90 degrees).
    
"""
from __future__ import print_function
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import leastsq

import numpy as np
import matplotlib.pyplot as plt

print(__doc__)

body_mass, work_level  = [], []  
heat_output = []
M, W, Y = [], [], []

# Read data from .dat file
def read_dat_file(file_path):
    file = open(file_path,"r") 
    lines = file.readlines() 
    file.close() 
    for line in lines:    
        body_mass.append(float(line.strip().split()[0]))
        work_level.append(float(line.strip().split()[1]))
        heat_output.append(float(line.strip().split()[2]))  

# Residuals = distance between data from dataset and estimated value
def residuals(p, y):
    a0, a1, a2, a3 = p
    
    # Difference between y data from dataset and estimated y value (using formula above)
    err = range(len(M))

    for j in range(len(M)):
        err[j] -= ( Y[j] - a0 - np.dot( a1, M[j] ) - W[j] / ( a2 + np.dot( a3, M[j] )))
    return err


# Plot the figure
def plot_figs(fig_num, elev, azim, a):
    fig = plt.figure(fig_num, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, elev=elev, azim=azim)

    ax.scatter(body_mass, work_level, heat_output, c='k', marker='+')
   
    X = np.arange(55, 85, 0.5)
    Y = np.arange(90, 180, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = a[0] + a[1]*X + +(Y/(a[2]+a[3]*X))
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
    read_dat_file('muscular_work.dat')

    # Shorten names
    M = body_mass
    W = work_level
    Y = heat_output
    
    # Our first guess for possible coefficien values
    p0 = [8, 7, 7, 8]
    print ('First guess: ', np.array(p0))
    
    # Minimize the sum of squares of a set of equations
    plsq = leastsq(residuals, p0, args=(Y))
    print ('LeastSq coefficients: ', plsq[0]) 
    
    # Generate the three different figures from different views
    a = [ plsq[0][0],plsq[0][1], plsq[0][2], plsq[0][3] ]    
    elev = 43.5
    azim = -110
    plot_figs(1, elev, azim, a)
    plt.title('(1) Least Square', color='g')
    
    elev = -.5
    azim = 0
    plot_figs(2, elev, azim, a)
    plt.title('(2) Least Square', loc='left', color='g')
    
    elev = -.5
    azim = 90
    plot_figs(3, elev, azim, a)
    plt.title('(3) Least Square', loc='right', color='g')
    
    plt.show()    
    
    
