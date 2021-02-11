import numpy as np

# 1
a = np.array([1, 4, 5, 8], float)
print(a)
type(a)

# 2
print(a[:2])
print(a[3])
a[0] = 5
print(a)

# 3
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(a)
print(a[0, 0])
print(a[0, 1])
