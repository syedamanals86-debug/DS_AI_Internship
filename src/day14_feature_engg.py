# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:08:28 2026

@author: Lenovo
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("2023 Car Dataset.csv")

df.columns = df.columns.str.strip()

# Applying Label Encoding to Transmission
le = LabelEncoder()
df["Transmission Type"] = le.fit_transform(df["Transmission Type"])
 
# Applying One-Hot Encoding to Color
df = pd.get_dummies(df, columns=["Color Options"], drop_first=True)


print("\nDataset after encoding:")
print(df.head())

# task 2

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


data = {
    "Age": [22, 25, 30, 35, 40, 28, 50, 48, 33, 26],
    "Salary": [25000, 30000, 50000, 70000, 90000, 45000, 120000, 110000, 60000, 35000]
}

df = pd.DataFrame(data)
X = df[["Age"]]
y = df["Salary"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -----------------------------
# Step 2: Linear Regression without scaling
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_orig = model.predict(X_test)
mse_orig = mean_squared_error(y_test, y_pred_orig)
print("MSE without scaling:", mse_orig)

# -----------------------------
# Step 3: StandardScaler
# -----------------------------
std_scaler = StandardScaler()
X_train_std = std_scaler.fit_transform(X_train)
X_test_std = std_scaler.transform(X_test)

model_std = LinearRegression()
model_std.fit(X_train_std, y_train)
y_pred_std = model_std.predict(X_test_std)
mse_std = mean_squared_error(y_test, y_pred_std)
print("MSE with StandardScaler:", mse_std)

# -----------------------------
# Step 4: MinMaxScaler
# -----------------------------
mm_scaler = MinMaxScaler()
X_train_mm = mm_scaler.fit_transform(X_train)
X_test_mm = mm_scaler.transform(X_test)

model_mm = LinearRegression()
model_mm.fit(X_train_mm, y_train)
y_pred_mm = model_mm.predict(X_test_mm)
mse_mm = mean_squared_error(y_test, y_pred_mm)
print("MSE with MinMaxScaler:", mse_mm)

# -----------------------------
# Step 5: Plot histogram (Age)
# -----------------------------
plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
plt.hist(X_train["Age"], bins=5)
plt.title("Original Age")

plt.subplot(1,3,2)
plt.hist(X_train_std, bins=5)
plt.title("Standardized Age")

plt.subplot(1,3,3)
plt.hist(X_train_mm, bins=5)
plt.title("Normalized Age")

plt.tight_layout()
plt.show()

# task 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# -----------------------------
# Step 1: Create synthetic non-linear dataset
# -----------------------------
np.random.seed(42)

# X = Age, y = Salary has a quadratic relationship
X = np.array([22, 25, 30, 35, 40, 28, 50, 48, 33, 26]).reshape(-1,1)
y = np.array([25000, 30000, 50000, 70000, 90000, 45000, 120000, 110000, 60000, 35000])

# -----------------------------
# Step 2: Linear Regression on original feature
# -----------------------------
lin_model = LinearRegression()
lin_model.fit(X, y)
y_pred_linear = lin_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)
print(f"R² with original feature: {r2_linear:.4f}")

# -----------------------------
# Step 3: Polynomial Features (degree=2)
# -----------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)  # Creates [Age, Age^2]

# Optional: visualize features
print("Polynomial features (first 5 rows):")
print(X_poly[:5])

# -----------------------------
# Step 4: Linear Regression on polynomial features
# -----------------------------
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)
print(f"R² with polynomial features: {r2_poly:.4f}")

# -----------------------------
# Step 5: Visual Comparison
# -----------------------------
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, y_pred_linear, color='red', label='Linear Regression')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Regression (degree=2)')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()


