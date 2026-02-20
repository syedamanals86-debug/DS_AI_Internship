# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 09:20:50 2026

@author: Lenovo
"""

import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Lenovo/Desktop/database/demo.db")

df = pd.read_sql_query("SELECT * FROM students",conn)

df = pd.read_sql_query("SELECT * FROM department",conn)

print(df)

# task 1

import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Lenovo/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT * FROM interns",conn)
df = pd.read_sql_query("SELECT name, track FROM interns",conn)

print(df)

