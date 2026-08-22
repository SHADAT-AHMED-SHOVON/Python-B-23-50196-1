import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([1, 4, 3, 8, 5, 2])

matching_positions = np.where(a == b)
print("Matching index positions:")
print(matching_positions[0])