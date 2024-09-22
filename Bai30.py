# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:49:46 2024

@author: ADMIN
"""

while True: 
    thang = int(input("Nhập vào tháng: "))
    nam = int(input("Nhập vào năm: "))
    if 1<= thang <= 12 and nam > 0:
        break 
    else: 
        print("Tháng hoặc năm chưa hợp lệ ")
so_ngay = 0 
if thang in (1, 3, 5, 7, 8, 10, 12 ):
    so_ngay = 31 
elif thang in(4, 6, 9, 11):
    so_ngay = 30
else: 
    if ( nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0 ):
        so_ngay = 29 
    else: 
        so_ngay = 28 
print(f"Tháng {thang} năm {nam} có số ngày là: {so_ngay}  ")