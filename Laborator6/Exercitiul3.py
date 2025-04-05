#Exercitiul 3

def bubbleSort(lista):
    N=len(lista)
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

if __name__=="__main__":
    lista = [16,4,17,13,9,6,8,5,10,11,7,3]
    print(bubbleSort(lista))
