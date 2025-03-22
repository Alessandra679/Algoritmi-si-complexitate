#Exercitiul 4

def este_crescator(a,n):
    index = range(1,n)
    for i in index:
        if a[i] < a[i-1]:
            return False
    return True
    
print(este_crescator([1,2,3,4,5],5))
print(este_crescator([1,2,3,5,4],5))
print(este_crescator([5,1,2,3,4],5))
