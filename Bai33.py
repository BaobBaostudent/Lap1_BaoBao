# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:43:01 2024

@author: ADMIN
"""


while True: 
    n = int(input("Nhập vào số nguyên dương: "))
    if n > 0:
        break 
    else: 
        print("Số chưa hợp lệ. Vui lòng nhập lại")
can_bac_hai = n**0.5 
if can_bac_hai.is_integer():
    print(f"{n} là số chính phương")
else:
    print(f"{n} không là số chính phương")