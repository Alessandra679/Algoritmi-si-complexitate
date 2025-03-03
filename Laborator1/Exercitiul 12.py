#Exercitiul 12

from math import sqrt

def ecuatie_gradII(a,b,c):
    delta = b**2-4*a*c
    if delta == 0:
        return -(b/(2*a))
    elif delta > 0:
        return (-b + sqrt(delta))/(2*a), (-b - sqrt(delta))/(2*a)
    else:
        return

print("Avem ecuatia de gr II: ax^2 + bx + c = 0")

a = float(input("a (nenul) = "))
b = float(input("b = "))
c = float(input("c = "))

print("Solutia: " + str(ecuatie_gradII(a,b,c)))