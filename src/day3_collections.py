# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 08:41:03 2026

@author: Lenovo
"""

# task 1
inventory = ["Apple","Banana", "Carrots", "Dates" ]
print(inventory)
inventory.append("Eggs")
print(inventory)
inventory.remove("Banana")
print(inventory)

#task 2
temprature = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(temprature[0])
print(temprature[-1])

afternoon_peak = temprature[3:6]
print("Afternoon Peak:", afternoon_peak )

last3_hours = temprature[-3:]
print("Last 3 Hours:" , last3_hours)

#task 3

screen_res = (1920,1080)
print("Current Resolution:", screen_res[0], "x", screen_res[1])

# screen_res[0] = 1280
print("Tuples cannot be modified!")



