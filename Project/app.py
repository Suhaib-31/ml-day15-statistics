import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("student_marks.csv")

marks = df["Marks"]

print("===== Statistics for ML =====\n")

# Mean
print("Mean:")
print(np.mean(marks))

# Median
print("\nMedian:")
print(np.median(marks))

# Mode
print("\nMode:")
print(marks.mode()[0])

# Minimum
print("\nMinimum:")
print(np.min(marks))

# Maximum
print("\nMaximum:")
print(np.max(marks))

# Range
print("\nRange:")
print(np.max(marks) - np.min(marks))

# Variance
print("\nVariance:")
print(np.var(marks))

# Standard Deviation
print("\nStandard Deviation:")
print(np.std(marks))

print("\nStatistics Analysis Completed!")