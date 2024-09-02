# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:20:53 2024

@author: ADMIN
"""

a = input("Nhập một ký tự: ")
if a.islower():
    kytu = a.upper()
else:
    kytu = a.lower()
print("Ký tự sau khi chuyển đổi: ", kytu)