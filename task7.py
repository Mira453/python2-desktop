import numpy as np

matrix = np.arange(1, 101).reshape(10, 10)

a = np.array2string(matrix, separator=', ' ,max_line_width=np.inf)
print(a)