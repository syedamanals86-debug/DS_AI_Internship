# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 09:55:40 2026

@author: Lenovo
"""
# task 1

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)
heights_df = pd.DataFrame(heights, columns=["Height"])


# plot histogram
plt.figure(figsize=(6,4))
sns.histplot(heights_df["Height"], kde=True, bins=30)
plt.title("Human Heights (Normal Distribution)")
plt.show()

# mean and median
mean_height = heights_df["Height"].mean()
median_height = heights_df["Height"].median()

print("Mean:", mean_height)
print("Median:", median_height)

# task 2

import numpy as np
import pandas as pd

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)

df = pd.DataFrame({"Height": heights})

# calculate height and std deviation
mu = df["Height"].mean()
sigma = df["Height"].std()

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

# calculate z- scores
df["z_score"] = (df["Height"] - mu) / sigma

df.head()

# task 3

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.exponential(scale=50000, size=100000)

df = pd.DataFrame({"Income": population})

# plot histogram for skewed data
plt.figure(figsize=(6,4))
sns.histplot(df["Income"], bins=50, kde=True)
plt.title("Original Population Distribution (Right-Skewed)")
plt.show()

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())

sample_means = pd.Series(sample_means)

# plot histogram for sample distrubution
plt.figure(figsize=(6,4))
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.show()







