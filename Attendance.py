# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:02:54 2019

@author: shinichikudo
"""

N = int(input("Enter number of classes held = ")) 
A = int(input("Enter Number of classes attended = "))
P = (A/N)*100
if P < 75.0:
        print(P)
        print('Not allowed to sit')             
else :
        print(P)
        print('Allowed to sit') 