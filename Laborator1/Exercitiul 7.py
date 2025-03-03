#Exercitiul 7

from math import sqrt
def f(x):
    if -1 < x < 1:
        return sqrt(x**2 + 1)
    else:
        return abs(x-3)
x = float(input("Introduceti un numar: "))
print(f(x))