# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:28:04 2024

@author: ADMIN
"""

gio_1 = int(input("Nhập giờ thứ nhất: "))
phut_1 = int(input("Nhập phút thứ nhất: "))
giay_1 = int(input("Nhập giây thứ nhất: "))

gio_2 = int(input("Nhập giờ thứ hai: "))
phut_2 = int(input("Nhập phút thứ hai: "))
giay_2 = int(input("Nhập giây thứ hai: "))

doi_1 = gio_1*3600 + phut_1*60 + giay_1 
doi_2 = gio_2*3600 + phut_2*60 + giay_2

tong = doi_1 + doi_2
hieu = doi_1 - doi_2

gio_tong = tong // 3600 
phut_tong = (tong // 3600 ) // 60 
giay_tong = (tong // 3600 ) % 60 

gio_hieu = hieu // 3600 
phut_hieu = (hieu // 3600 ) // 60 
giay_hieu = (hieu // 3600 ) % 60 

print(f"Tổng hai khoảng thời gian là: {gio_tong} giờ, {phut_tong} phút, {giay_tong} giây")
print(f"Hiệu hai khoảng thời gian là: {gio_hieu} giờ, {phut_hieu} phút, {giay_hieu} giây")


