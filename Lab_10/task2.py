import numpy as np

arr = np.array([10, 20, 30, 20, 50, 20])
target_value = 20

indices = np.where(arr == target_value)
print("Positions of value 20:")
print(indices[0])