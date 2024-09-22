# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:32:10 2024

@author: ADMIN
"""

s = 0 
ts = 0
ms = 1 
n = int(input("Nhập vào n: "))
while n<=0:
    n = int(input("Nhập vào n > 0: "))
x = float(input("Nhập vào x: "))
for i in range(1, n+1 ):
    ts = x**i 
    ms = ms + i 
    s += ts/ms 
print(round(s,2))