# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:52:46 2024

@author: PC
"""

a, b, c, n = 2, 7, 9, 979
max_sum = 0
solutions = []
for x in range(1, n // a + 1):
    for y in range(1, (n - a * x) // b + 1):
        if (n - a * x - b * y) % c == 0:
            z = (n - a * x - b * y) // c
            if z > 0:
                current_sum = x + y + z
                if current_sum > max_sum:
                    max_sum = current_sum
                    solutions = [(x, y, z)]
                elif current_sum == max_sum:
                    solutions += [(x, y, z)]
print("Các bộ nghiệm có tổng lớn nhất:")
for sol in solutions:
    print(sol)