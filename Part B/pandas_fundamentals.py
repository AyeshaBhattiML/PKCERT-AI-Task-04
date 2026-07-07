# ==========================================
# PKCERT Internship Task 04
# Part B - Pandas Fundamentals
# ==========================================

import pandas as pd

print("===== 1. Creating Pandas Series =====")

# Create a Series
students = pd.Series(
    [85, 90, 78, 92, 88],
    index=["Ali", "Ayesha", "Ahmed", "Sara", "Fatima"]
)

print(students)

print("\n===== 2. Creating DataFrame =====")

data = {
    "Name": ["Ali", "Ayesha", "Ahmed", "Sara", "Fatima"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["AI", "CS", "AI", "SE", "CS"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df)

print("\n===== 3. Indexing and Selection =====")

print("\nNames Column:")
print(df["Name"])

print("\nFirst Three Rows:")
print(df.head(3))

print("\nRow with Index 2:")
print(df.loc[2])

print("\nName and Marks Columns:")
print(df[["Name", "Marks"]])

print("\n===== 4. Filtering =====")

high_marks = df[df["Marks"] > 85]

print("Students with Marks greater than 85:")
print(high_marks)

print("\n===== 5. Sorting =====")

sorted_df = df.sort_values(by="Marks", ascending=False)

print("Sorted by Marks (Highest to Lowest):")
print(sorted_df)

print("\n===== 6. GroupBy =====")

group = df.groupby("Department")["Marks"].mean()

print("Average Marks by Department:")
print(group)

print("\n===== 7. Merging DataFrames =====")

attendance = pd.DataFrame({
    "Name": ["Ali", "Ayesha", "Ahmed", "Sara", "Fatima"],
    "Attendance": [90, 95, 85, 92, 88]
})

merged = pd.merge(df, attendance, on="Name")

print(merged)

print("\n===== 8. Joining DataFrames =====")

grades = pd.DataFrame({
    "Grade": ["B", "A", "C", "A", "B"]
})

joined = df.join(grades)

print(joined)