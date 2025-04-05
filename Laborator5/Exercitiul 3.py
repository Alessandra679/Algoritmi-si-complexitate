def combinari_Recursiv(n,k):
    if k ==0 or k == n:
        return 1
    return combinari_Recursiv(n-1,k-1) + combinari_Recursiv(n-1,k)

def test_combinari(functie):
    assert(functie(4,0) == 1), "Test picat pt k=0"
    assert(functie(4,4) == 1), "Test picat pt k=n"
    assert(functie(4,2) == 6), "Test picat pt nr naturale"
    print(functie.__name__ + " a trecut testele")

test_combinari(combinari_Recursiv)
print(combinari_Recursiv(4,2))