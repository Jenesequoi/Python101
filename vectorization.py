import numpy as np
array = np.array(range(5))
array**= 2
print(array)
a= array
print(f"The shape of this array is {a.shape}")
print(f"The number of dimensions of this array is {a.ndim}")
print(f"The number of elements in this array is {a.size}")

b= np.array([[1, 2, 3],
             [4, 5, 6]])
b
print(f"The shape of this array is {b.shape}")
print(f"The number of dimensions is {b.ndim}")
print(f"The number of elements is {b.size}")