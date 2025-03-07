def creare_lista(n):
    lista = []
    for i in range (0,n):
        lista.append(int(input("Dati elementul " + str(i) + ": ")))
    return lista
if __name__ == "__main__":
    print(creare_lista(10))
