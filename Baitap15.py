# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:41:41 2024

@author: ADMIN
"""

import math 
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

bt1 = (a + b) / math.sqrt(a + b) - math.pow(a*b, 1/3)
bt2 =  math.pow(math.pow(a, 1/3) - math.pow(b, 1/3), 2)
 

Tong =  bt1/bt2 
print ("Kết quả của biểu thức: ", Tong)