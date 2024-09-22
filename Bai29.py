# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:42:55 2024

@author: ADMIN
"""

while True: 
    n = int(input("Nhập vào số nguyên dương: "))
    if n > 0:
        break 
    else: 
        print("Vui lòng nhập lại vào số nguyên dương")
tong = 0 
while n > 0: 
    chu_so = n % 10 
    tong += chu_so 
    n = n //  10 
print(f"Tổng các chữ số của {n} là: ", tong)