import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame({
    "marks": np.random.randint(0, 101, size=50)
})

# Plot histogram
plt.hist(df["marks"], bins=10)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Student Marks")
plt.show()
