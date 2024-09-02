# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:49:28 2024

@author: ADMIN
"""
import math
a = float(input("Nhập vào bán kính hình tròn: "))
chu_vi = 2 * math.pi * a
dien_tich = math.pi * a ** 2
print("Chu vi của hình tròn là: ", round(chu_vi, 2))
print("Diện tích của hình tròn là: ", round(dien_tich, 2))
