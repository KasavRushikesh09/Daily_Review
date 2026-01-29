import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    "name": ["Rushi", "dhiraj", "ram", "nike", "sham"],
    "age": [18, np.nan, 35, np.nan, 78]
})

print("df:")
print(df)

mean_age = df["age"].mean()

df["age"].fillna(mean_age, inplace=True)
print(df)
plt.bar(df["name"], df["age"],color =[ "yellow","grey","red"])
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("aage of People")
plt.show()
