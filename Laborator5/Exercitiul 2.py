def cautare_binara(lista, x, st, dr):
    if st>dr:
        return -1
    mij = (st+dr) // 2 #(catul intreg)
    if lista[mij] == x:
        return mij
    elif lista[mij]>x:
        return cautare_binara(lista, x, st, mij-1)
    else:
        return cautare_binara(lista,x, mij+1, dr)
lista = [0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
element = 9.9
print(cautare_binara(lista, element, 0, len(lista)-1))