import os
import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "titanic.csv")
df = pd.read_csv(file_path)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

plt.figure()
plt.plot(df['Fare'].head(50).values, marker='o', color='blue')
plt.title("Line Plot - Fare of First 50 Passengers")
plt.xlabel("Passenger Index")
plt.ylabel("Fare")
plt.show()

plt.figure()
plt.scatter(df['Age'], df['Fare'], color='darkgreen', alpha=0.5)
plt.title("Scatter Plot - Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

plt.figure()
pclass_counts = df['Pclass'].value_counts()
plt.bar(pclass_counts.index.astype(str), pclass_counts.values, color='coral')
plt.title("Bar Chart - Passenger Count by Class")
plt.xlabel("Ticket Class (Pclass)")
plt.ylabel("Number of Passengers")
plt.show()

plt.figure()
plt.hist(df['Age'], bins=10, color='purple', edgecolor='black')
plt.title("Histogram - Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
gender_counts = df['Sex'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart - Passenger Gender Distribution")
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

survived_counts = df['Survived'].value_counts()
axes[0].bar(['Died (0)', 'Survived (1)'], survived_counts.values, color=['red', 'green'])
axes[0].set_title("Survival Count")
axes[0].set_ylabel("Count")

axes[1].hist(df['Fare'], bins=10, color='teal', edgecolor='black')
axes[1].set_title("Fare Distribution")
axes[1].set_xlabel("Fare")

plt.tight_layout()
plt.show()