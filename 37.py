# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:40:27 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương chẵn n: "))
if n > 0 and n % 2 == 0:
    S = sum(i for i in range(2, n + 1, 2))
    print(f"Tổng S từ 2 đến {n} là: {S}")
else:
    print("Số nhập vào phải là số chẵn và lớn hơn 0.")