import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import chisquare
from scipy.stats import shapiro
import seaborn as sns

# # # # Task 1

# Определение случайной последовательности и её длины
n = 1000000
mass = [random.uniform(0, 1) for i in range(n)]
# print(mass)

# График случайной величины

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x=range(10000), y=mass[0:10000])
# plt.show()


# # Task 1.1

# Расчёт мат. ожидания

m_squared = []
eval_math = float("{0:.2f}".format(sum(mass) / n))

for i in mass:
    m_squared.append(float("{0:.5f}".format(pow(i, 2))))

# Расчёт дисперсии

dispersion = (float("{0:.3f}".format((sum(m_squared) / n) - pow(eval_math, 2))))

# Вывод результатов

print("Dispersion:", dispersion)
print("Expected value:", eval_math)






# # Task 1.2

# Функция правильного округления

def to_round(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
# Сортировка массива

mass.sort()
# Определение интервалов

m = to_round(1 + 3.322 * math.log(n,10))
r = mass[-1] - mass[0]
h = r / m
# Вывод количества интервалов

# print(m)
# Вспомогательные переменные
f_elem = mass[0]
intervals = []
table = PrettyTable()
frequency = 0
index = 1
freq_sum = 0
dict_freq = {}
table = PrettyTable()

# Определение столбцов
table.field_names = ['Index', 'Interval', 'Frequency hit', 'Relative frequency ']

# Создание интервалов
for i in range(m):
    intervals.append((round(f_elem, 4), round(f_elem + h, 4)))
    f_elem += h
    
# Заполнение таблицы данными
for interval in intervals:
    for num in mass:
        if interval[0] <= num < interval[1]:
            frequency += 1
    table.add_row([index, interval, frequency, frequency / n])
    dict_freq[interval] = frequency
    frequency = 0
    index += 1
# Подсчёт суммы частот
for key in dict_freq:
    freq_sum += dict_freq[key]
    
# Добавление суммы в таблицу
table.add_row([' ', ' ', ' ', ' '])
table.add_row(['Σ', ' ', freq_sum, ' '])

# Вывод таблицы
print(table)


# # Task 1.3

values_listed = list(dict_freq.values())
average_interval = []
teor_frequency = []
it_value = 0

for interval in intervals:
    average_interval.append( (interval[0] + interval[1]) / 2)


average = sum(average_interval)/len(average_interval)
average_squared_deviation = math.sqrt(np.var(average_interval))

a1 = average - math.sqrt(3) * average_squared_deviation
b1 = average + math.sqrt(3) * average_squared_deviation
f1 = 1/(b1-a1)

for interval in intervals:
    if not it_value:
        teor_frequency.append(n * f1 * (interval[1] - a1))
    elif it_value == (len(intervals) - 1):
        teor_frequency.append(n * f1 * (b1 - interval[0]))
    else:
        teor_frequency.append(n * f1 * (interval[1] - interval[0]))

    it_value += 1


res = chisquare(values_listed, f_exp=teor_frequency)

print("Statistic:", res[0],"\n", res[1])

# Вывод гистограммы
pd.Series(dict_freq).plot.bar()
plt.show()


# Task 1.4

# # Функция правильного округления
def to_round(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num 


# Функция создания распределения
def generatorUniDistribution(m):
    uni_distribution = np.array([random.uniform(0,1) for i in range(m)])
    return uni_distribution

# Заполнение массива максимумов
maxes = []
for i in range(1000000):
    maxes.append(generatorUniDistribution(1000).max())
# print("Array of maxes = ", maxes)

# Вывод гистограммы
sns.histplot(maxes)
plt.show()


