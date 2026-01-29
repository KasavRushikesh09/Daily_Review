from helper.helper1 import sample_data
import matplotlib.pyplot as plt
import pandas as pd

#Task 1
def trend_across_days(df):
    total_sales = df.groupby('day')['sales'].sum()
    return total_sales

#Task2


if __name__ == '__main__':
    df = sample_data()
    print(f"Sample Data:\n{df}")

    trend = trend_across_days(df)
    print(f"Trend Across Day:\n{trend}")

    plt.plot(trend.index, trend.values, color="red")
    plt.xlabel("Day")
    plt.ylabel("Total Sales")
    plt.title("Sales Trend Across Days")
    plt.grid()
    plt.show()
