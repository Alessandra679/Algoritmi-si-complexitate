#Exercitiul 5(2)

def este_simetrica2(matrice,n):
    for i in range(n):
        for j in range(i):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True
    
AA = [[1,2,3],[2,3,4],[3,4,5]]
print(este_simetrica2(AA,3))

