#Exercitiul 8

from math import sqrt,sin

a = float(input("Introduceti primul numar (nenul): "))
b = float(input("Introduceti al doilea numar (nenul): "))

def functie(x,y):
    if abs(x) <= 8 and abs(y) <= 8:
        valoare = ((a*b)/sqrt(x**2 + y**2)) * sin(sqrt(x**2 + y**2))
    else:
        valoare = 0
    return valoare

print(functie(0, 3))