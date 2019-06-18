# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:23:38 2019

@author: SinichiKudo
"""

import numpy as np
import scipy.stats as si
import sympy as sy

def G_BlackScholes_1(S, X, T, r, v, CallPutFlag):
    d1=float((np.log(S/X)+(r+0.5*v*v)*T)/(v*np.sqrt(T)))
    d2=float(d1-v*np.sqrt(T))
    GBlackScholes=0.000
    
    if CallPutFlag == 'c':
        GBlackScholes = (S * si.norm.cdf(d1, 0.0, 1.0) - X * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    elif CallPutFlag == 'p':
        GBlackScholes = (X * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    print(GBlackScholes)
        
G_BlackScholes_1(60.00,65.00,0.25,0.08,0.3,'c')
     
#S: spot price 
#X: strike price
#T: time to maturity
#r: interest rate
#v: volatility of underlying asset
    
S=60.00
X=65.00
T=0.25
r=0.08
v=0.3
CallPutFlag='c'














#import sympy.statistics as systats