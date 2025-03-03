#Exercitiul 9

from math import sqrt

#prima cerinta din problema
def numar_perfect1(x):
    s = 0
    x = abs(x)
    for i in range(1,x):
        if x % i == 0:
            s += i
    if(s == x):
        return True
    else:
        return False

x = int(input("Introduceti un numar natural: "))
print(numar_perfect1(x))

#a doua cerinta din problema

def numar_perfect2(x):
    x = abs(x)
    for i in range(1, x+1):
        if numar_perfect1(i):
            print(i, end=' ')

numar = int(input("Introduceti inca un numar: "))
numar_perfect2(numar)
