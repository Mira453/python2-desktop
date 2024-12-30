import numpy as np

matrix = np.random.randint(1, 100, (5, 5))
print(matrix)

max_in_rows = np.max(matrix, axis=1)
print("Найбільші елементи в кожному рядку: ", max_in_rows)

min_in_rows = np.min(matrix, axis=1)
print("Найменший елемент в кожному рядку: ", min_in_rows)

max_in_columns = np.max(matrix, axis=0)
print("Найбільші елементи в кожному стовпці:", max_in_columns)

min_in_columns = np.min(matrix, axis=0)
print("Найменші елементи в кожному стовпці:", min_in_columns)