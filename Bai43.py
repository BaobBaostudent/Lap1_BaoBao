# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:26:46 2024

@author: ADMIN
"""

s = 0 
n = int(input("Nhập vào n: "))
while n<=0:
    n = int(input("Nhập vào n > 0: "))
for i in range(1, n+1 ):
    s += i/(i+1) 
print(round(s,2))