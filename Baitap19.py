# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:18:36 2024

@author: ADMIN
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))

min_number = a

if b < min_number:
    min_number = b
if c < min_number:
    min_number = c
if d < min_number:
    min_number = d

print("Số nhỏ nhất là:", min_number)