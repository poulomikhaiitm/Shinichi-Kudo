#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:50:00 2019

@author: gokul
"""
import random as rd

def rand4(x1,x2):
    a=rd.randint(0,3)
    if a==0:
        return x1-1,x2
    elif a==1:
        return x1+1,x2
    elif a==2:
        return x1,x2-1
    else:
        return x1,x2+1

def rand3(x1,x2,res):
    a=rd.randint(0,2)
    if res==0:
        if a==0:
            return x1+1,x2
        elif a==1:
            return x1,x2-1
        else:
            return x1,x2+1
    elif res==1:
        if a==0:l
            return x1-1,x2
        elif a==1:
            return x1+1,x2
        else:
            return x1,x2-1
    elif res==2:
        if a==0:
            return x1-1,x2
        elif a==1:
            return x1,x2+1
        elif a==2:
            return x1,x2-1
    else:
        if a==0:
            return x1-1,x2
        elif a==1:
            return x1+1,x2
        elif a==2:
            return x1,x2+1

def rand2(x1,x2,res):
    a=rd.randint(0,1)
    if res==0:
        if a==0:
            return x1+1,x2
        elif a==1:
            return x1,x2-1
    elif res==1:
        if a==0:
            return x1-1,x2
        elif a==1:
            return x1,x2-1
    elif res==2:
        if a==0:
            return x1-1,x2
        elif a==1:
            return x1,x2+1
    elif res==4:
        if a==0:
            return x1,x2-1
        elif a==1:
            return x1,x2+1
    else:
        if a==0:
            return x1,x2+1
        elif a==1:
            return x1+1,x2
f1=[]
for i in range(1000000):
    x1=0
    x2=0
    f=0
    while (x1!=50 or x2!=50):
        if (x1,x2)==(0,0):
            x1,x2=rand2(x1,x2,3)
        elif (x1,x2)==(100,0):
            x1,x2=rand2(x1,x2,2)
        elif (x1,x2)==(100,100):
            x1,x2=rand2(x1,x2,1)
        elif (x1,x2)==(0,100):
            x1,x2=rand2(x1,x2,0)
        elif x1==0 and (x2!=0 and x2!=100):
            x1,x2=rand3(x1,x2,0)
        elif x1==100 and (x2!=0 and x2!=100):
            x1,x2=rand3(x1,x2,2)
        elif x2==100 and (x1!=0 and x1!=100):
            x1,x2=rand3(x1,x2,1)
        elif x2==0 and (x1!=0 and x1!=100):
            x1,x2=rand3(x1,x2,3)
        else:
            x1,x2=rand4(x1,x2)
        f+=1
    f1.append(f) 
    print(i)   
f2=sum(f1)/len(f1)
print(f2)