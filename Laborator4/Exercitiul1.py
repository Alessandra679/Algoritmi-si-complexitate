# Exercitiul 1

def norm(a):
    s = 0
    for element in a:
        s += (element*element)
    return s**0.5
#sau

def norm1(a,n):
    s=0
    for i in range(n):
        s += (a[i]*a[i])
    return s**0.5

a = [3,4,12]
print(norm(a))
print(norm1(a,3))