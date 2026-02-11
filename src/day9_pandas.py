# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:19:21 2026

@author: Lenovo
"""

# Task 1

import pandas as pd

products = pd.Series([700,150,300], index = ("Laptop", "Mouse", "Keyboard"))
print(products)

# access the price of laptop
print(products["Laptop"])

# slice
firsts2 = products[0:2]
print(firsts2) 

# Task 2

grades = pd.Series([85, None, 92, 45, None, 78, 55])
print(grades.isnull())

print(grades.fillna(0))

# boolean masking
greater = grades[grades > 60]
print(greater)
# or
print(grades[grades > 60])

# Task 3

username = pd.Series(['Alice', 'bOB', ' Charlie_Data', 'daisy'])
print(username)
# remove white space
print(username.str.strip())

# convert to lowercase
low = username.str.lower()
print(low)

# all names containing the letter a
print(low.str.contains('a'))
