# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:28:12 2024

@author: PC
"""
N= int(input("Nhập vào số nguyên dương N: "))
if N > 0:
    print("N thoã mãn")
else:
    print("N phải là số nguyên dương. Vui lòng nhập lại.")
print(f"Tất cả các ước số của {N} là:")
for i in range(1, N+1):
    if N % i == 0:
        print(i)

