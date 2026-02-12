# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 09:39:42 2026

@author: Lenovo
"""

import pandas as pd

data = {
"OrderID": [1001,1002,1003,1004,1004,1005],
"CustomerID": [201,202,203,204,204,205],
"Name": ["Rahul","Anita","Sarah","Sneha","Sneha","Vikram"],
"Age": [29,None,34,None,None,31],
"City": ["Delhi "," Mumbai","Chennai","Bangalore","Bangalore","Goa"],
"ProductCategory": ["Electronics","Clothing","Groceries","Clothing","Clothing",None],
"OrderAmount": [5000,2200,None,3500,3500,None],
"Discount": [500,None,200,350,350,None],
"PaymentMethod": ["Card","UPI","Cash",None,None,"UPI"],
"DeliveryStatus": ["Delivered","Shipped","Delivered","Delivered","Delivered","Delivered"],
"Date": ["2024-01-02","2024-01-15","2024-02-03",
         "2024-03-05","2024-03-05","2024-03-12"]
}

df = pd.DataFrame(data)

# before cleaning
print("First rows:\n", df.head())
print("\nDataset info:")
print(df.info())

# Check missing values
print("\nMissing values per column:")
print(df.isna().sum())

# Handling missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].median())
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])

# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nFinal cleaned dataset:")
print(df.head())


# task 2
data2 = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": ["$1,200", "$800", "$450", "$300", "$150"],
    "Date": ["2024-01-05", "2024-01-10", "2024-02-01", "2024-02-15", "2024-03-01"]
}

df = pd.DataFrame(data2)

# check initial data types
print("\nInitial Data Types:\n")
print(df.dtypes)

# removing $ symbols
df["Price"] = ( df["Price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float))

# convert date coloumn 
df["Date"] = pd.to_datetime(df["Date"])

print(df)

# Task 3
# Sample 
data = {
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles "],
    "OrderAmount": [250, 300, 150, 400, 350]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# normalization
# Remove  whitespace
df["Location"] = df["Location"].str.strip()

# Standardize casing 
df["Location"] = df["Location"].str.title()

print("\nNormalized DataFrame:\n")
print(df)

# verify
print("\nUnique Locations:\n", df["Location"].unique())
