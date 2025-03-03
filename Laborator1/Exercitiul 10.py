#Exercitiul 10

#prima cerinta din problema

def suma_cifrelor_lui_n(n):
    s = 0
    while n != 0:
        s = s + n%10
        print(s)
        n = int(n/10)
    return s
n = int(input("Introduceti un numar natural: "))
print(suma_cifrelor_lui_n(n))

#a doua cerinta din problema

def inversarea_cif_lui_n(n):
    nr_nou = 0
    while n != 0:
        nr_nou = nr_nou*10 + n%10
        n = int(n/10)
    return nr_nou
n = int(input("Introduceti un numar natural: "))
print(inversarea_cif_lui_n(n))

#a treia cerinta din problema

def reprezentare_n_in_baza2(n):
    nr_nou = 0
    p = 1
    while n!=0:
        c = n%2
        nr_nou = nr_nou + c*p
        p *= 10
        n = int(n/2)
    return nr_nou
n = int(input("Introduceti un numar natural: "))
print(reprezentare_n_in_baza2(n))

#a patra cerinta din problema

from math import sqrt

def numar_prim(n):
    prim = True
    if n<2 or (n>2 and n % 2 == 0):
        prim = False
    for d in range(3,int(sqrt(n))+1):
        if n % d == 0:
            prim = False
    if prim == True:
        print("Numarul introdus este numar prim")
    else:
        print("Numarul introdus nu este numar prim")

n = int(input("Introduceti un numar natural: "))
numar_prim(n)

