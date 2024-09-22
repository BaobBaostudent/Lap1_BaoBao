# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:29:31 2024

@author: ADMIN
"""

a = float(input("Nhập vào số Km: "))
if a <= 1:
    st = 15  
    print("Số tiền phải trả là: ", st);
elif 2 <= a <= 5:
    st= 1*15 + (a-1)*13.5 
    print("Số tiền phải trả là: ", st);
elif a > 6:
    st=1*15 + (a-1)*13.5 + (a-6)*11 
    print("Số tiền phải trả là: ", st);
if a > 120:
    stc = st*0.9 
    print("Số tiền sau giảm giá là: ", stc)
