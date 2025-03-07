def citire_matrice(linii, coloane):
     matrice = []
     for i in range(0, linii):
        matrice.append([])
        for j in range(0, coloane):
            matrice[i].append(input("Dati elementul["+str(i)+"]["+str(j)+"]="))
     return matrice
def afisare_matrice(matrice):
     for i in range(0, len(matrice)):
        for j in range(0, len(matrice[0])):
            print(matrice[i][j], end=" ")
        print()
if __name__ == '__main__':
     m = citire_matrice(2,3)
     afisare_matrice(m)
