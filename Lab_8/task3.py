import pandas as pd

df = pd.read_csv("titanic.csv")

print("--- First 5 rows (Head) ---")
print(df.head())

print("\n--- Last 5 rows (Tail) ---")
print(df.tail())

print("\n--- Dataset Summary (Info) ---")
df.info()