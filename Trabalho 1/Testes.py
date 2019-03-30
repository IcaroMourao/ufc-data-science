import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[1,2]])

print(a)
print(b)
print(b.shape)

b = np.insert(b, 1, a[0], axis=0)
a = np.delete(a, 0, axis=0)

print(a)
print(b)
print(b.shape)