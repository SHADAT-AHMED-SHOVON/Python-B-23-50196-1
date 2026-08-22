import numpy as np

arr = np.array([12, 5, 8, 1, 19, 3, 7])
k = 3

k_smallest = np.partition(arr, k)[:k]
print("K-smallest values:")
print(np.sort(k_smallest))