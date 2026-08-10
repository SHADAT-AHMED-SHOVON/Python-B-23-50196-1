import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
s = pd.Series(calories)

print("Pandas Series:")
print(s)

total_calories = s.sum()
print("\nSummation of calories:", total_calories)