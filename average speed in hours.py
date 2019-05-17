# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:55:34 2019

@author: shinichikudo
"""

K = int(input('Enter no.of kilometers = '))
S1 = int(input('Enter Time in minutes ='))
S2 = int(input('Enter Time in seconds ='))
S3 = (S1/60) # from minutes to hours 
S4 = (S2/3600) # from seconds to hours
T = S3 + S4
AS = (K/T) #average pace 
print(AS)
print(T)