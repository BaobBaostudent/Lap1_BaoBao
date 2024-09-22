# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:50:38 2024

@author: ADMIN
"""


n = int(input("Nhập vào số nguyên dương lớn hơn 1: "))
while n<= 0:
    print("Số chưa hợp lệ")
    break 
    if n < 2: 
        print("Không phải là số nguyên tố")
    
    else:   
        for i in range(2, n+1 ):
            if n % i == 0: 
                print("Không phải là số nguyên tố")
                break 
            else:
                print("Là số nguyên tố")
                break 
        


