import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

selected_rows = df.loc[[0, 2]]
print(selected_rows)