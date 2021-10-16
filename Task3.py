
import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import chisquare
from scipy.stats import shapiro
import seaborn as sns

n = 100

# Task 3
def pos_value(a):
    a = float(a)
    if a < 0:
        print("\nErorr, incorrect input")
        a = float(input("\nEnter correct value: "))
    return a

def gauss():
    gauss_ = []
    mu = float(input("Enter mu: "))
    sigma = pos_value(input("Enter sigma: "))
    for i in range(100):
        gauss_.append(float("{0:.5f}".format(random.gauss(mu, sigma))))

    # Вывод графика
    plt.plot(gauss_[:100])
    plt.show()

    print('Mathematical expectation and dispersion for gauss: ', round(np.mean(gauss_), 5), round(np.var(gauss_), 5))


    def to_round(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    gauss_.sort()
    m = to_round(1 + 3.322 * math.log(100, 10))
    r = gauss_[-1] - gauss_[0]
    h = r / m

    f_elem = gauss_[0]
    intervals = []
    table = PrettyTable()
    frequency = 0
    index = 1
    # freq_sum = 0
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
        for num in gauss_:
            if interval[0] <= num < interval[1]:
                frequency += 1
        table.add_row([index, interval, frequency, frequency / n])
        dict_freq[interval] = frequency
        frequency = 0
        index += 1

    # Вывод таблицы
    print(table)
    # Вывод гистограммы
    pd.Series(dict_freq).plot.bar()
    plt.show()



def weibull():
    weibull_ = []
    alpha = float(input("Enter alpha: "))
    beta = float(input("Enter beta: "))
    for i in range(100):
        weibull_.append(float("{0:.5f}".format(random.weibullvariate(alpha, beta))))
    plt.plot(weibull_[:100])
    plt.show()

    print('Mathematical expectation and dispersion for weibull: ', round(np.mean(weibull_), 5), round(np.var(weibull_), 5))

    def to_round(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    weibull_.sort()
    m = to_round(1 + 3.322 * math.log(100, 10))
    r = weibull_[-1] - weibull_[0]
    h = r / m

    f_elem = weibull_[0]
    intervals = []
    table = PrettyTable()
    frequency = 0
    index = 1
    # freq_sum = 0
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
        for num in weibull_:
            if interval[0] <= num < interval[1]:
                frequency += 1
        table.add_row([index, interval, frequency, frequency / n])
        dict_freq[interval] = frequency
        frequency = 0
        index += 1

    # Вывод таблицы
    print(table)
    # Вывод гистограммы
    pd.Series(dict_freq).plot.bar()
    plt.show()

def rayleigh():
    mode = pos_value(input("Enter mode: "))
    rayleigh_ = np.random.rayleigh(mode, 100)
    plt.plot(rayleigh_[0:5])
    plt.show()

    print('Mathematical expectation and dispersion for reyleigh: ', round(np.mean(rayleigh_), 5), round(np.var(rayleigh_), 5))
    
    def to_round(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    rayleigh_.sort()
    m = to_round(1 + 3.322 * math.log(100, 10))
    r = rayleigh_[-1] - rayleigh_[0]
    h = r / m

    f_elem = rayleigh_[0]
    intervals = []
    table = PrettyTable()
    frequency = 0
    index = 1
    # freq_sum = 0
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
        for num in rayleigh_:
            if interval[0] <= num < interval[1]:
                frequency += 1
        table.add_row([index, interval, frequency, frequency / n])
        dict_freq[interval] = frequency
        frequency = 0
        index += 1

    # Вывод таблицы
    print(table)
    # Вывод гистограммы
    pd.Series(dict_freq).plot.bar()
    plt.show()


def lognormal():
    lognormal_ = []
    mulognormal = float(input("Enter mu for logNormal distribution: "))
    sigmalognormal = pos_value(input("Enter sigma for logNormal distribution: "))
    for i in range(100):
        lognormal_.append(float("{0:.5f}".format(random.lognormvariate(mulognormal, sigmalognormal))))
    plt.plot(lognormal_[:100])
    plt.show()

    print('Mathematical expectation and dispersion for logNormal: ', round(np.mean(lognormal_), 5), round(np.var(lognormal_), 5))

    def to_round(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    lognormal_.sort()
    m = to_round(1 + 3.322 * math.log(100, 10))
    r = lognormal_[-1] - lognormal_[0]
    h = r / m

    f_elem = lognormal_[0]
    intervals = []
    table = PrettyTable()
    frequency = 0
    index = 1
    # freq_sum = 0
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
        for num in lognormal_:
            if interval[0] <= num < interval[1]:
                frequency += 1
        table.add_row([index, interval, frequency, frequency / n])
        dict_freq[interval] = frequency
        frequency = 0
        index += 1

    # Вывод таблицы
    print(table)
    # Вывод гистограммы
    pd.Series(dict_freq).plot.bar()
    plt.show()


def cauchy():
    cauchy_ = np.random.standard_cauchy(100)
    plt.plot(cauchy_[:100])
    plt.show()

    print('Mathematical expectation and dispersion for cauchy: ', round(np.mean(cauchy_), 5), round(np.var(cauchy_), 5))

    def to_round(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    cauchy_.sort()
    m = to_round(1 + 3.322 * math.log(100, 10))
    r = cauchy_[-1] - cauchy_[0]
    h = r / m

    f_elem = cauchy_[0]
    intervals = []
    table = PrettyTable()
    frequency = 0
    index = 1
    # freq_sum = 0
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
        for num in cauchy_:
            if interval[0] <= num < interval[1]:
                frequency += 1
        table.add_row([index, interval, frequency, frequency / n])
        dict_freq[interval] = frequency
        frequency = 0
        index += 1

    # Вывод таблицы
    print(table)
    # Вывод гистограммы
    pd.Series(dict_freq).plot.bar()
    plt.show()




def start():

    print("Choose the distribution:\n1 - Normal\n2 - Weibull\n3 - Rayleigh\n4 - LogNormal\n5 - Cauchy")
    number = int(input(""))

    if number == 1:
        gauss()
        again()
    elif number == 2:
        weibull()
        again()   
    elif number == 3:
        rayleigh()
        again()
    elif number == 4:
        lognormal()
        again()
    elif number == 5:
        cauchy()
        again()
    else:
        print("Wrong number!")


def again():
    print("Would you like to try again?:\n1 - yes\n2 - no")
    choice = int(input(""))
    if choice == 1:
        start()
    
    elif choice == 2:
        return 0 


start()


