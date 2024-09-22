# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:28:26 2024

@author: ADMIN
"""

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
       
if a + b > c and a + c > b and b + c > a:
    print("Ba số đã nhập có thể tạo thành một tam giác.")
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Ba số đã nhập không thể tạo thành một tam giác.")