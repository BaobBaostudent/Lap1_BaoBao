# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:39:22 2024

@author: ADMIN
"""

time = input("Nhập vào giờ, phút và giây (Theo định dạng hh:mm:ss): ")
hh,mm,ss = map(int, time.split(":"))
if 0 <= hh < 24 and 0 <= mm <60 and 0 <= ss < 60:
    Doi = hh*3600 + mm*60 + ss
    print ("Số giây là: ", Doi)
else:
    print("Giờ, phút và giây chưa hợp ")