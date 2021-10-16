import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import chisquare
from scipy.stats import shapiro

# Task 5
## Создание бинарной последовательности
length = int(input("Enter the quantity of random numbers:\n=> "))
mass = np.random.standard_cauchy(length)
binary_mass = {1: 0, 0: 0}

for i in range(0, length - 1):
    if mass[i+1] - mass[i] > 0:
        binary_mass[1] += 1
    elif mass[i+1] - mass[i] <= 0:
        binary_mass[0] += 1

for key in binary_mass:
    binary_mass[key] = binary_mass[key] / length


## Построение гистограммы
plt.bar(binary_mass.keys(), binary_mass.values(), width=0.1)
plt.show()