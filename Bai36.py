# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:05:34 2024

@author: ADMIN
"""

while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Số chưa hợp lệ. Vui lòng nhập lại")
S = 0
for i in range(1, (n+1)**2 ):
    S += i

print("Tổng S =", S)