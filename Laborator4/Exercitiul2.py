#Exercitiul 2

def suma_matrice(A,B,n):
    index = range(n)
    C = []
    for i in index:
        C.append([])
        for j in index:
            C[i].append(A[i][j]+B[i][j])
    return C

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,1,1],[1,1,1],[1,1,1]]

print(suma_matrice(A,B,3))