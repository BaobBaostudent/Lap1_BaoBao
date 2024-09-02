# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:10:58 2024

@author: ADMIN
"""

a = int(input("Nhập số giờ: "))
b = int(input("Nhập số phút: "))
c = int(input("Nhập số phút: "))
if a<= 24 and b<= 60 and c<=60:
    Doi = a*3600 + b*60 + c
    print(f"{a} giờ {b} phút {c} giây tương đương với {Doi} giây")
else:
    print("Giờ, phút và giây không hợp ")