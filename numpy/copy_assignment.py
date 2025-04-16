import numpy as np
from numpy.ma.core import arange

lis = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr * 2)
print(matrix * 2)

print("=" * 60)

zeros = np.zeros((3, 4))
print(zeros)

ones = np.ones((2, 3))
print(ones)

eye = np.eye(4)
print(eye)

linspace = np.linspace(0, 10, 5)
print(linspace)

arange = np.arange(0, 10, 3)
print(arange)

