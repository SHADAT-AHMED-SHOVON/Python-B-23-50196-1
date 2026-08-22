import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6]])

col_sums = np.sum(mat, axis=0)
row_sums = np.sum(mat, axis=1)

print("Column-wise sum:")
print(col_sums)
print("Row-wise sum:")
print(row_sums)