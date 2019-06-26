# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:38:05 2019

@author: SinichiKudo
"""

from itertools import combinations 
comb = combinations([1, 2, 3], 2)   
for i in list(comb): 
    print i                                                                    # Get all combinations of [1, 2, 3] 
                                                                               # and length 2   
                                                                               # Print the obtained combinations 
