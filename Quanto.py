# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:23:38 2019

@author: SinichiKudo
"""

import numpy as np
import scipy.stats as si
import sympy as sy

def Quanto_1(S, X, T, r, rf, q, vS, vE, rho, Ep, CallPutFlag = 'call'):
    
    d1= float((np.log(S/X)+(rf-q-rho*vS*vE+0.5*vS*vS)*T)/(vS*np.sqrt(T)))
    d2=float(d1-vS*np.sqrt(T))
    
   
    
    if CallPutFlag == 'call':
        Quanto = Ep * (S * np.exp((rf-r-q-rho * vS * vE) * T) * si.norm.cdf(d1, 0.0, 1.0) - X * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    else:
        Quanto = Ep * (X * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp((rf-r-q-rho * vS * vE) * T) * si.norm.cdf(-d1, 0.0, 1.0))
   
    print(Quanto)    
    


#Quanto_1(75.00,70.00,0.50,0.10,0.05,0.35,'call')  
    
    
#S: spot price
#X: strike price
#T: time to maturity
#r: interest rate
#v: volatility of underlying asset
    


    
        