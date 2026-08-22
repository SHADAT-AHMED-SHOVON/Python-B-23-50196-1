import numpy as np

arr = np.array([10, -5, 20, -15, 30, -1])
arr[arr < 0] = 0

print("Array after replacing negative values with zero:")
print(arr)