# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:45:30 2024

@author: ADMIN
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

SLN = a
if b > SLN:
    SLN = b
if c > SLN:
    SLN = c
print("Số lớn nhất là: ", SLN)