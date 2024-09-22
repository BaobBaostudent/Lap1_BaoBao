# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:38:58 2024

@author: ADMIN
"""

n = -1 
while n<=0:
    n=int(input("Nhập vào số nguyên:"))
print(f"Ước của số {n} là:")
for i in range(1, n+1):
    if n % i ==0:
        print(i)