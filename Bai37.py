# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:06:58 2024

@author: ADMIN
"""

while True:
        n = int(input("Nhập số nguyên dương chẵn: "))
        if n > 0 and n % 2 == 0:
            break
        else:
            print("Số chưa hợp lệ. Vui lòng nhập lại")
S = 0
for i in range(2, n+1, 2):
    S += i

print("Tổng S =", S)