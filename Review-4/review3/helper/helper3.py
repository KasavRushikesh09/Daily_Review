from faker import Faker
import pandas as pd

def task_three():
    fk = Faker()
    department_list = [i for i in range(10)]
    min_salary = 10000
    max_salary = 80000

    department =[]
    salary = []

    data = {
        'department' : department,
        'salary' : salary
    }

    for _ in  range(1000):
        department.append(fk.random_element(department_list))
        salary.append(fk.random_int(min_salary,max_salary))
    return pd.DataFrame(data)

if __name__  == '__main__':
    print(task_three())
