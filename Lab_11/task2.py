import numpy as np

arr = np.array([10, 20, 30, 20, 40, 20, 50])
target_item = 20
n = 2

indices = np.where(arr == target_item)[0]
if len(indices) >= n:
    print(f"Index of occurrence {n} for value {target_item}:", indices[n - 1])
else:
    print("Occurrence not found")