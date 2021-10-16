import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy import random
from scipy.stats import chisquare

# Монте карло 1
def first_integral():
    def f(x):
	    return (x**7 + x**5 + x**3)  
    a = 0
    b = 1 
    N = 1000000
    ar = np.zeros(N)
    for i in range (len(ar)):
        ar[i] = random.uniform(a,b)

    integral = 0.0

    for i in ar:
        integral += f(i)

    ans = (b-a)/float(N)*integral

    print ("The value calculated by monte carlo integration is {0:.5f}.".format(ans))

# Монте карло 2

def second_integral():

    def f(x):
	    return (2*np.sin(3*x))
    a = 0
    b = np.pi
    N = 1000000
    ar = np.zeros(N)
    for i in range (len(ar)):
        ar[i] = random.uniform(a,b)

    integral = 0.0

    for i in ar:
        integral += f(i)

    ans = (b-a)/float(N)*integral

    print ("The value calculated by monte carlo integration is {0:.5f}.".format(ans))



#  Монте карло 3 

def third_integral():

    def f(x):
        tanX = np.tan(x)
        return (1 / (( tanX + 1 ) * np.sqrt(tanX)) ) * (2 / (np.cos(2 * x) + 1))

    a = 0
    b = np.pi/2
    N = 100000
    ar = np.zeros(N)
    for i in range (len(ar)):
        ar[i] = random.uniform(a,b)

    integral = 0.0

    for i in ar:
        integral += f(i)

    ans = (b-a)/float(N)*integral

    print ("The value calculated by monte carlo integration is {0:.5f}.".format(ans))

def start():
    print("Choose integral that you want to solve:\n1 - (x**7 + x**5 + x**3) from 0 to 1\n2 - (2*np.sin(3*x)) from 0 to pi\n3 - 1/((x+1)sqrt(x)) from 0 to ∞")
    number = int(input(""))

    if number == 1:
        first_integral()
        again()
    elif number == 2:
        second_integral()
        again()   
    elif number == 3:
        third_integral()
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


