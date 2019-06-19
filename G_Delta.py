# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:23:38 2019

@author: SinichiKudo
"""

import numpy as np
import scipy.stats as si
import sympy as sy

def G_Delta_1(S, X, T, r, b, v, CallPutFlag = 'call'):
    
    d1=float((np.log(S/X)+(b+0.5*v*v)*T)/(v*np.sqrt(T)))
 
    if CallPutFlag == 'call':
        G_Delta =  np.exp((b-r) * T) * si.norm.cdf(d1, 0.0, 1.0) 
    elif CallPutFlag == 'p':
        G_Delta = -np.exp((b-r) * T) * si.norm.cdf(-d1, 0.0, 1.0)
    print(G_Delta)    
    


G_Delta_1(105.00,100.00,0.50,0.1,0.00,0.36,'p')   

    
    
#S: spot price
#X: strike price
#T: time to maturity
#r: interest rate
#v: volatility of underlying asset
    


    
        