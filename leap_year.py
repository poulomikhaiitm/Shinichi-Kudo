# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:21:26 2019

@author: SinichiKudo
"""


def is_leap(year):
        
        if year % 400 ==0:
            return True
        if year % 100 ==0:
            return False
        if year % 4 ==0:
            return True
        else:
            return False
year = int(input("Enter the year = "))
print(is_leap(year))