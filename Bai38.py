# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:09:02 2024

@author: ADMIN
"""

while True:
        n = int(input("Nhập số nguyên dương lẻ n: "))
        if n > 0 and n % 2 != 0:
            break
        else:
            print("Số chưa hợp lệ. Vui lòng nhập lại")
S = 1 
for i in range(1, n+1):
    S *= i 
print("Tích S =", S)