# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:50:07 2022

@author: VOL2SZ
"""

L1 = [1,2,3,4,5,6,7,8,9]
L2 = []
move = 0
teiler = 5

for i in range(teiler-1):
    move = L1.pop(0)
    L2.append(move)
     
        
print(L1)
print(L2)