# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:04:22 2024

@author: ADMIN
"""

a = float(input("Nhập vào số thứ nhất: "))
b = float(input("Nhập vào số thứ hai: "))
c = float(input("Nhập vào số thứ ba: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b +delta**0.5) / (2*a)
    x2 = (-b -delta**0.5) / (2*a)
    print("Phương trình có hai nghiệm phân biệt: ")
    print("x1 = ", x1)
    print("x2 = ", x2)
elif delta == 0:
    print("Phương trình có nghiệm kép: x = ", -b/(2*a))
else:
    print("Phương trình vô nghiệm")