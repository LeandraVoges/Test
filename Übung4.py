# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:28:47 2022

@author: VOL2SZ
"""
"""
x = 6
y = 80
"""
x = input("Zahl1 zum Tauschen eingeben")
y = input("Zahl2 zum Tauschen eingeben")
def tauschen(a, b):
    chng = a
    a = b
    b = chng
    print (a)
    print (b)
    
tauschen(x , y)