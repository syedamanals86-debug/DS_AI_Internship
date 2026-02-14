# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 21:07:34 2026

@author: Lenovo
"""
# Day 12 task 1

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.scatter(study_hours, scores)

plt.xlabel("Hours Spent Studying")
plt.ylabel("Exam Score")
plt.show()