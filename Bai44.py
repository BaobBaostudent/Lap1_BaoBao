# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:30:40 2024

@author: ADMIN
"""

s = 0 
n = int(input("Nhập vào n: "))
while n<=0:
    n = int(input("Nhập vào n > 0: "))
for i in range(1, n+1 ):
    s += (2*i+1)/(2*i+2) 
print(round(s,2))