def list_of_indices(lista, valoarea):
     indici = []
     for index in range(0, len(lista)):
        if lista[index] == valoarea:
            indici.append(index)
     return set(indici)
if __name__=="__main__":
    print(list_of_indices([1,2,3,4,1,2,1],1))