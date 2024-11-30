import numpy as np 

a = np.array([float(i) for i in range(1, 101)])
print(a)

b = np.reshape(a, (10, 10))
print(b)