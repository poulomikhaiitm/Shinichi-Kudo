# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:58:55 2019

@author: SinichiKudo
"""


class employee:
    def __init__(self, first,last, salary):  #self will be first it just a way of indenting it
        self.first = first
        self.last = last
        self.salary = salary
        
        first = raw_input("enter the first name =")
        last =  raw_input("enter the first name =")
        salary = int(input("enter the value"))
emp_1 = employee(first,last,salary)

print(emp_1)
