# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:41:07 2024

@author: PC
"""

def tinh_tong(n):
  tong = 0
  for i in range(1, n+1):
    tong += 1 / i
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)