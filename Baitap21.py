# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:50:18 2024

@author: ADMIN
"""

so = int(input("Nhập một số:  "))
so_bang_chu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
if 0<= so<= 9:
    print("Số bằng chữ là: ", so_bang_chu[so])
else:
    print("Không đọc được")