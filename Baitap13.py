# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:01:04 2024

@author: ADMIN
"""

a = int(input("Nhập ngày sinh: "))
b = int(input("Nhập tháng sinh: "))
c = int(input("Nhập năm sinh: "))

print(f"{a}/{b}/{c}")
print(f"{a}/{b}/{str(c)[-2:]}")
print(f"{c}/{b}/{a}")