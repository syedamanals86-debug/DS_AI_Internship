# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:28:38 2026

@author: Lenovo
"""
#Task 1

contacts = {"Ahmed": 99455887624 , "Sarah": 2244789962 , "Maryam": 2468879524}
print(contacts)

# Add new contact
(contacts["Abdul"]) = 2548961321
# Update existing Contact
(contacts["Sarah"]) = 8547961203
print(contacts)

# Use of .get() method 

print(contacts.get("Maryam")) # for existing contact
print(contacts.get("Fatima", "contact not found")) # for non exeistent name

# iteration

for Contact,Phone in contacts.items():
    print(Contact,Phone)

# Task 2

# Create list
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Create set
unique_users = set(raw_logs)
print(unique_users)

# Membership test
print("ID05" in unique_users)

# Print the length of list and set
print(len(raw_logs), len(unique_users))  
print(unique_users)

# Task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

print(friend_a & friend_b)
print(friend_a | friend_b)
print(friend_a - friend_b)
