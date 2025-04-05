def putere(a,n):
    if n==0:
        return 1
    if n>0:
        return (a*putere(a,n-1))
    if n<0:
        return 1/a*putere(a,n+1)

x = int(input("Introduceti un numar: "))
a = int(input("Introduceti un alt numar: "))

print("x^a = " + str(putere(x,a)))
