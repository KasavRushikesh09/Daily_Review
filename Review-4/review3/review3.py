import pandas as pd
import matplotlib.pyplot as plt

data = {
    "department": ["HR", "IT", "Finance", "HR", "IT", "Finance", "IT", "HR"],
    "salary": [30000, 50000, 60000, 32000, 52000, 58000, 54000, 31000]
}

df = pd.DataFrame(data)
print(df)
avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)
plt.bar(avg_salary.index, avg_salary.values)
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary per Department")
plt.grid(axis="y")
plt.show()
