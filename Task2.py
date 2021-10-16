import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import chisquare

# Task 2
# Определение массивов величин и вероятностей
x_array = np.array([7, 16, 28, 33, 39, 46, 56])
p_array = np.array([0.01, 0.05, 0.07, 0.1, 0.17, 0.25, 0.35])
mass = [round(random.random(), 5) for i in range(1000)]

# График случайной величины
fig1, ax1 = plt.subplots(figsize=(10, 10))
plt.plot(x_array, p_array)
ax1.set_xlabel('x')
ax1.set_ylabel('p')

# Вывод графика
# plt.show()





# Task 2.1
# Вспомогательные переменные
eval_math = 0
dispersion = 0

# Вычисление дисперсии и мат ожидания
for i in range(len(x_array)):
    eval_math += (x_array[i] * p_array[i])
    dispersion += (pow(x_array[i], 2) * p_array[i])
dispersion -= pow(eval_math, 2)


# Вывод полученных значений
print("Expected value:", eval_math)
print("Dispersion:", round(dispersion, 3))




# Task 2.2
# Функция правильного округления
def rounding(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

# Вспомогательные переменная
x0 = 0
intervals = []
dict_freq = {}
count = 0
index = 1
summa = 0

# Построение интервалов
for i in range(7):
    intervals.append((float("{0:.5f}".format(x0)), float("{0:.5f}".format(x0 + p_array[i]))))
    x0 += p_array[i]
#print(intervals)


# Создание объекта таблицы
table1 = PrettyTable()
table1.field_names = ['Index', 'Interval', 'Frequency hit', 'Relative frequency']

# Заполнение таблицы данными
for interval in intervals:
  for num in mass:
    if interval[0] <= num < interval[1]:
      count +=1
  table1.add_row([index, interval, count, round(count/1000, 3)])
  dict_freq[interval] = count
  count = 0
  index += 1

# Подсчёт суммы частот
for key in dict_freq:
    summa += dict_freq[key]

# Добавление суммы в таблицу
table1.add_row([' ', ' ', ' ', ' '])
table1.add_row(['Σ', ' ', summa, ' '])

# Вывод таблицы
print(table1)

# Тask 2.3
# Построение гистограммы
pd.Series(dict_freq).plot.bar()
plt.show()