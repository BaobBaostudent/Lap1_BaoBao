# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:35:43 2024

@author: ADMIN
"""

a = float(input("Nhập vào số có 2 chữ số: "))
shc = a//10
shdv = a%10
Tong = shc+shdv
if 10<= a <=99:
    print("Tổng của 2 chữ số là: ", Tong)
else:
    print("Số không hợp lệ")