# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 10:12:43 2026

@author: Lenovo
"""

def cal_rectangle(length, width):
    area = length * width
    perimeter = 2 * length + width
    return area, perimeter
 
length = int(input("Enter length: "))
width = int(input("Enter width: "))

X, Y = cal_rectangle(length, width)

print("Area:", X, "Perimeter:", Y)




