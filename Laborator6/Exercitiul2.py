#Exercitiul 2

def sortare_selectie_minim(lista):
    N=len(lista)
    for j in range(0,N-1):
        m = j
        for i in range(j+1,N):
            if lista[m] > lista[i]:
                m = i
            if(m != j):
                aux = lista[m]
                lista[m] = lista[j]
                lista[j] = aux
    return lista

if __name__=="__main__":
    lista = [3,4,2,5,7,1]
    print(sortare_selectie_minim(lista))
 