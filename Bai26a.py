# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:25:40 2024

@author: ADMIN
"""

a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))
c = int(input("Nhập vào số thứ ba: "))

thu_tu = [a, b, c]
sap_xep = sorted(thu_tu)

print("Các số theo thứ tự tăng dần: ", sap_xep  )