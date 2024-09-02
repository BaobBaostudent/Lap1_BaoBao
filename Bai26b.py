# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:43:06 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên: "))
chuoi = list(str(a))
chuoi.sort()
chuyen_chuoi = int("".join(chuoi))
print("Các chữ số theo thứ tự tăng dần là: ", chuyen_chuoi )