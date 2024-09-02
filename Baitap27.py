# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:55:25 2024

@author: ADMIN
"""

import math 
hinh = input("Nhập hình (v: vuông, n: nhật, t: tròn): ")
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh: "))
    chu_vi = canh * 4 
    dien_tich = canh ** 2 
    print("Chu vi hình vuông: ", chu_vi)
    print("Diện tích hình vuông: ", dien_tich)
elif hinh == 'n':
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    chu_vi = 2 * (a+b)
    dien_tich = a*b
    print("Chu vi hình chữ nhật: ", chu_vi)
    print("Diện tích hình chữ nhật: ", dien_tich)
elif hinh == 't':
    r = float(input("Nhập bán kính: "))
    chu_vi = 2 * math.pi * r
    dien_tich = math.pi * r**2
    print("Chu vi hình tròn: ", chu_vi)
    print("Diện tích hình tròn: ", dien_tich)
else:
    print("Hình không hợp lệ")
    