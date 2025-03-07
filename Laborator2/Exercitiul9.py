from Exercitiul4 import creare_lista
from Exercitiul6b import list_of_indices
def ciurul_lui_Eratostene(n):
    lista = []
    for k in range(0,n):
        lista.append(True)
    for i in range(2,n):
        for j in range(i+1,n):
            if j%i == 0:
                lista[j] = False
    return lista
if __name__ == "__main__":
    n = int(input("Introduceti un numar: "))
    l=ciurul_lui_Eratostene(n)
    print(list_of_indices(l,True))