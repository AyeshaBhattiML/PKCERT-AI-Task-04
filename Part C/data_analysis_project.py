# ==========================================
# PKCERT Internship Task 04
# Part C - Data Analysis Mini Project
# Loan Dataset Analysis
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r"C:\Users\Ayesha\Documents\loan_data.csv")

# Display first five rows
print("\nFirst Five Rows")
print(df.head())

# Dataset information
print("\nDataset Information")
df.info()

# Dataset shape
print("\nDataset Shape")
print(df.shape)

# Column names
print("\nColumn Names")
print(df.columns)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Check if missing values exist
if df.isnull().sum().sum() == 0:
    print("\nNo missing values found in the dataset.")
else:
    print("\nDataset contains missing values.")

# Summary statistics
print("\nSummary Statistics")
print(df.describe())

# Gender distribution
print("\nGender Distribution")
print(df["person_gender"].value_counts())

# Education distribution
print("\nEducation Distribution")
print(df["person_education"].value_counts())

# Home ownership
print("\nHome Ownership Distribution")
print(df["person_home_ownership"].value_counts())

# Loan intent
print("\nLoan Intent Distribution")
print(df["loan_intent"].value_counts())

# Loan status
print("\nLoan Status")
print(df["loan_status"].value_counts())

# Average values
print("\nAverage Person Age")
print(df["person_age"].mean())

print("\nAverage Person Income")
print(df["person_income"].mean())

print("\nAverage Loan Amount")
print(df["loan_amnt"].mean())

print("\nAverage Credit Score")
print(df["credit_score"].mean())

# GroupBy operations
print("\nAverage Income by Gender")
print(df.groupby("person_gender")["person_income"].mean())

print("\nAverage Loan Amount by Education")
print(df.groupby("person_education")["loan_amnt"].mean())

print("\nAverage Credit Score by Home Ownership")
print(df.groupby("person_home_ownership")["credit_score"].mean())

print("\nLoan Status by Loan Intent")
print(df.groupby("loan_intent")["loan_status"].value_counts())

# Filtering
print("\nApplicants with Income Greater Than 100000")
print(df[df["person_income"] > 100000][
    ["person_age", "person_income", "loan_amnt"]
])

print("\nApplicants with Loan Amount Greater Than 15000")
print(df[df["loan_amnt"] > 15000][
    ["person_age", "loan_amnt", "loan_intent"]
])

# Sorting
print("\nTop 10 Highest Income Applicants")
print(df.sort_values(by="person_income", ascending=False).head(10))

# -----------------------------
# Data Visualization
# -----------------------------

# Gender Distribution
df["person_gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Loan Status Distribution
df["loan_status"].value_counts().plot(kind="bar")
plt.title("Loan Status Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Count")
plt.show()

# Education Distribution
df["person_education"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Education Distribution")
plt.ylabel("")
plt.show()

# Person Income Histogram
plt.hist(df["person_income"], bins=20)
plt.title("Person Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

# Loan Amount Histogram
plt.hist(df["loan_amnt"], bins=20)
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.show()

print("\nData Analysis Completed Successfully!")