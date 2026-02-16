# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 21:21:21 2026

@author: Lenovo
"""

# Day 12 task 2

import matplotlib.pyplot as plt

# Bar Chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# line plot (example)
months = [1, 2, 3, 4, 5]
monthly_sales = [800, 950, 900, 1100, 1200]

# Subplot 1: Bar Chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales, color=['blue', 'green', 'orange'])
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Subplot 2: Line Plot 
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")


# Prevent overlap
plt.tight_layout()

plt.show()
