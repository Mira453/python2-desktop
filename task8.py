import numpy as np

matrix = np.arange(1, 101).reshape(1, 100)
print(matrix)
      
matrix.shape = (100, 1)
print(matrix)