import numpy as np
#Vector math in NumPy: dot and norm


u = np.array([1.0, 2.0, 3.0])
v = np.array([2.0, 0.0, 1.0])

res = np.dot(u, v)
res2 = u @ v

#dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = a @ b # or: np.dot(a, b)
print(dot) # 1*4 + 2*5 + 3*6 = 32