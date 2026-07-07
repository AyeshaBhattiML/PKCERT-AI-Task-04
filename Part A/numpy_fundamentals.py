# ==========================================
# PKCERT Internship Task 04
# Part A - NumPy Fundamentals
# ==========================================

import numpy as np

print("===== 1. Creating NumPy Arrays =====")

# From a list
array1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(array1)

# Two-dimensional array
array2 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\n2D Array:")
print(array2)

# Using arange()
array3 = np.arange(1, 11)
print("\nArray using arange():")
print(array3)

# Using zeros()
zeros = np.zeros((2, 3))
print("\nZeros Array:")
print(zeros)

# Using ones()
ones = np.ones((3, 2))
print("\nOnes Array:")
print(ones)

# Using linspace()
lin = np.linspace(0, 10, 5)
print("\nLinspace Array:")
print(lin)


print("\n===== 2. Indexing and Slicing =====")

print("First Element:", array1[0])
print("Last Element:", array1[-1])

print("\nFirst Three Elements:")
print(array1[:3])

print("\nSecond Row:")
print(array2[1])

print("\nElement at Row 1 Column 2:")
print(array2[0, 1])


print("\n===== 3. Reshaping =====")

numbers = np.arange(1, 13)
print("Original Array:")
print(numbers)

reshaped = numbers.reshape(3, 4)
print("\nReshaped (3x4):")
print(reshaped)


print("\n===== 4. Mathematical Operations =====")

a = np.array([5, 10, 15])
b = np.array([2, 4, 6])

print("Addition:")
print(a + b)

print("Subtraction:")
print(a - b)

print("Multiplication:")
print(a * b)

print("Division:")
print(a / b)

print("Square:")
print(a ** 2)

print("Square Root:")
print(np.sqrt(a))


print("\n===== 5. Broadcasting =====")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

vector = np.array([10, 20, 30])

print("Matrix:")
print(matrix)

print("\nVector:")
print(vector)

print("\nBroadcasting Result:")
print(matrix + vector)


print("\n===== 6. Vectorized Operations =====")

numbers = np.arange(1, 11)

# Traditional Loop
loop_result = []

for i in numbers:
    loop_result.append(i * 2)

print("Loop Result:")
print(loop_result)

# Vectorized
vector_result = numbers * 2

print("\nVectorized Result:")
print(vector_result)


print("\n===== 7. Linear Algebra =====")

matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nDot Product:")
print(np.dot(matrix1, matrix2))

print("\nMatrix Multiplication:")
print(np.matmul(matrix1, matrix2))

print("\nTranspose:")
print(matrix1.T)

print("\nInverse:")
print(np.linalg.inv(matrix1))