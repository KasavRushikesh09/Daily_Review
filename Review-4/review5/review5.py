import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame({
    "hours_studied": [8,4,6,2,3,4,5,9],
    "score": [40, 45, 50, 60, 65, 70, 78, 85]
})

print(df)
plt.scatter(df["hours_studied"], df["score"],color = "violet")
plt.xlabel("hours studied")
plt.ylabel("score")
plt.title("hours studied vs score")
plt.show()

