# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:24:02 2024

@author: ADMIN
"""

s = 0 
n = int(input("Nhập vào n: "))
while n<=0:
    n = int(input("Nhập vào n > 0: "))
for i in range(1, n+1 ):
    s += 1/2*i  
print(round(s,2))