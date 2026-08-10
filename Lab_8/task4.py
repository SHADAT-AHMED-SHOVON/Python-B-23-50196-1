import pandas as pd

df = pd.read_csv("titanic.csv")

df = df.drop_duplicates()

if 'Age' in df.columns:
    df['Age'] = df['Age'].fillna(df['Age'].mean())

if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

if 'Cabin' in df.columns:
    df = df.drop(columns=['Cabin'])

if 'Age' in df.columns:
    df['Age'] = df['Age'].astype(int)

print("Cleaned Dataset Info:")
df.info()