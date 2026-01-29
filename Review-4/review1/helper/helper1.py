from faker import Faker
import pandas as pd

def sample_data():
    fk = Faker()
    days_list = list(i for i in range(1,8))

    min_sale = 100
    max_sale = 500

    day = []
    sales = []

    data = {
       'day' : day,
       'sales' : sales,
    }
    for _ in range(1000):
        day.append(fk.random_element(days_list))
        sales.append(fk.random_int(min_sale,max_sale))

    return pd.DataFrame(data)

if __name__ == '__main__':
    print(sample_data())




