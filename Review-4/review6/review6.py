import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker

fk = Faker()

name_list = []

for _ in range(50):
    name_list.append(fk.first_name())

print(name_list)

# import random
#
# df = pd.DataFrame({
#
#      'Gender' : [random.choice(['Male','Female']). i for i in range(100)]
# })

