# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:00:19 2024

@author: PC
"""

thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))

# Kiểm tra xem năm có phải là năm nhuận hay không
nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

# Số ngày trong các tháng
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay = 30
elif thang == 2:
    if nam_nhuan:
        so_ngay = 29  # Tháng 2 có 29 ngày nếu là năm nhuận
    else:
        so_ngay = 28  # Tháng 2 có 28 ngày nếu không phải năm nhuận
else:
    so_ngay = 0  # Tháng không hợp lệ

if so_ngay > 0:
    print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
else:
    print("Tháng không hợp lệ.")
