# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 09:37:32 2026

@author: Lenovo
"""
# task 1
name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
     file.write("Name: " + name + " | Daily Goal: " + goal + "\n")

# task 2
import csv 
with open("students.csv",'r') as file:
     reader = csv.DictReader(file)
     for row in reader:
       if row["Status"] == "Pass":
           print(row["Name"])

# task 3

try:
    with open("config.txt",'r') as file:
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")