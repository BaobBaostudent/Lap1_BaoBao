# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:02:36 2024

@author: ADMIN
"""

a = float(input("Nhập vào số cân năng của bạn (kg): "))
b = float(input("Nhập vào số chiều cao của bạn (m): "))
BMI = a/(b**2)
print("Chỉ số BMI của bạn là: ")
if BMI < 18.5:
    print("Bạn đang thiếu cân")
elif 18.5 <= BMI <24.9:
    print("Bạn đang bình thường")
elif 25 <= BMI < 29.9:
    print("Bạn đang thừa cân")
else:
    print("Bạn bị béo phì")
