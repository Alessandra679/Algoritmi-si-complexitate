def multimea_cif_lui_n(n):
    copie = n
    Mc = []
    while copie:
        Mc.append(copie % 10)
        copie = copie//10
    m = len(Mc)
    for i in range(0,10):
        while Mc.count(i) > 1:
            Mc.pop(Mc.index(i))
    Mc.sort()
    return set(Mc)

if __name__=="__main__":
    n = int(input("Introduceti un numar natural: "))
    print(multimea_cif_lui_n(n))

