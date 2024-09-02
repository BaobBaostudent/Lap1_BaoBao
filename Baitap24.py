# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:11:24 2024

@author: ADMIN
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 23 and 0 <= phut<= 59 and 0 <= giay<= 59:
    print("Giờ, phút, giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ")