import numpy as np

#From Python lists (dtype inferred)

a = np.array([1, 2, 3])
b = np.array([1.0, 2.5, 3.0])
#[1 2 3] int64  (dtype may be int32/int64 depending on platform)
print(a, a.dtype)
#[1.  2.5 3. ] float64
print(b, b.dtype)

#Explicit dtype

c = np.array([1, 2, 3], dtype=np.float32)
#[1. 2. 3.] float32
print(c, c.dtype)

#Attributes

#shape: (3,)
print("shape:", c.shape)
#number_dimensions: 1
print("ndim:", c.ndim)
#size: 3
print("size:", c.size)
#itemsize: 4 (for float32)
print("itemsize:", c.itemsize, "bytes")
#nbytes: 12
print("nbytes:", c.nbytes)