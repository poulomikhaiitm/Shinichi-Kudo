# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:57:17 2019

@author: SinichiKudo
"""
import QuantLib as ql
Month = int(input("Enter the valuation month = "))
Date = int(input("Enter the valuation day = "))
Year = int(input("Enter the valuation year = "))
VDate = ql.Date(Month, Date, Year)
print("VDate")
