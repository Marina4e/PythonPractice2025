import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 8]
])

print(matrix[1:, :2])

arr = np.arange(1, 13)
print(arr)
reshaped = arr.reshape((3, 4))
print(reshaped)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

hstack = np.vstack((arr1, arr2))
print(hstack)

print(np.mean(arr1))

print(np.std(arr1))



