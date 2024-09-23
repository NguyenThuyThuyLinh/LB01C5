# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:39:03 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    S = sum(i**2 for i in range(1, n + 1))
    print(f"Tổng S từ 1^2 đến {n}^2 là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")