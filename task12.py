import numpy as np

matrix = np.random.randint(1, 100, (8, 8))
print(matrix)

number = 68
bool_matrix = matrix > number
print(bool_matrix)

count = np.sum(bool_matrix)
print(f"Кількість елементів більших за {number}: {count}")