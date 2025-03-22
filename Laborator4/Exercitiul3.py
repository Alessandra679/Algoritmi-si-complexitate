#Exercitiul 3

def produs_matrice_vector(matrice,vector,n,m):
    rezultat = []
    for i in range(n):
        rezultat.append(0)
        for j in range(m):
            rezultat[i] += matrice[i][j]*vector[j]
    return rezultat
    
A = [[1,2,3],[4,5,6]]
X = [1,1,1]
print(produs_matrice_vector(A,X,2,3))