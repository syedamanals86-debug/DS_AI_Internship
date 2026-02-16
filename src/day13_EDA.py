# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 10:52:08 2026

@author: Lenovo
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

df = pd.read_csv("housing.csv")
df.head()

# plotting histogram
plt.figure()
sns.histplot(df["price"], kde=True)
plt.title("Price Distribution")
plt.show()

# calculate skewness and kurtosis
price_skewness = skew(df["price"])
price_kurtosis = kurtosis(df["price"])

print("Skewness:", price_skewness)
print("Kurtosis:", price_kurtosis)

# for categorical data
plt.figure()
sns.countplot(x="airconditioning", data=df)
plt.title("Air Conditioning")
plt.show()

# Task 2
# Scatter plot
plt.figure()

plt.subplot(1,2,1)
sns.scatterplot(x="area", y="price", data=df)
plt.title("Area vs Price")

# Box plot
plt.subplot(1,2,2)
sns.boxplot(x="parking", y="prefarea", data=df)
plt.title("Parking vs Prefarea")

plt.tight_layout()
plt.show()

print("Scatter Plot Observation:")
print("As area increases, price seems to increase.")


print("\nBox Plot Observation:")
print("As parking increases, prefarea seems to increase.")

#task 3

# Select only numeric columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Generate correlation matrix
corr_matrix = numeric_df.corr()

# Plot heatmap
plt.figure()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')

plt.title("Correlation Matrix Heatmap")
plt.show()

# Boxplot for Outliers
plt.figure
sns.boxplot(y=df["price"])
plt.title("Boxplot of House Prices")
plt.show()

# Print correlation values
print(corr_matrix)


