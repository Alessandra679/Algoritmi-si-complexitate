#Exercitiul 1

def sortare_selectie_maxim(lista):
    N = len(lista)
    for i in range(N-1,0,-1):
        m=0
        for j in range(1,i+1):
            if lista[m]<lista[j]:
                m=j
            if m != i:
                aux = lista[m]
                lista[m] = lista[i]
                lista[i] = aux
    return lista

if __name__=="__main__":
    lista=[3,1,2,4,5,9,8]
    print(sortare_selectie_maxim(lista))