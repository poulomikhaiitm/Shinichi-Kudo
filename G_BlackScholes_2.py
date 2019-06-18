# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:23:38 2019

@author: SinichiKudo
"""

import numpy as np
import scipy.stats as si
import sympy as sy

def G_BlackScholes_2(S, X, T, r, b, v, CallPutFlag = 'call'):
    
    d1=float((np.log(S/X)+(b+0.5*v*v)*T)/(v*np.sqrt(T)))
    d2=float(d1-v*np.sqrt(T))
    
    if CallPutFlag == 'call':
        GBlackScholes = S * np.exp((b-r) * T) * si.norm.cdf(d1, 0.0, 1.0) - X * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
    else:
        GBlackScholes = X * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp((b-r) * T) * si.norm.cdf(-d1, 0.0, 1.0)
   
    print(GBlackScholes)    
    


G_BlackScholes_2(75.00,70.00,0.50,0.10,0.05,0.35,'call')  
    
    
#S: spot price
#X: strike price
#T: time to maturity
#r: interest rate
#v: volatility of underlying asset
    


    
        