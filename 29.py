# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:44:10 2024

@author: PC
"""
N = int(input("Nhập vào số nguyên dương N: "))
tong = 0
while N > 0:
    chu_so = N % 10  # Lấy chữ số cuối cùng
    tong += chu_so   # Cộng chữ số vào tổng
    N = N // 10      # Bỏ chữ số cuối cùng

print(f"Tổng các chữ số là: {tong}")
