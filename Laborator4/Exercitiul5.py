#Exercitiul 5

def este_simetrica(matrice,n):
    index = n
    for i in range(n):
        for j in range(n):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True
    
AA = [[1,2,3],[2,3,4],[3,4,5]]
print(este_simetrica(AA,3))

