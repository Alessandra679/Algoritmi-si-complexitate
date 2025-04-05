#Combinari - cod interativ

#Varianta lenesa (si mai putin eficienta)

def combinari_Iterativ(n,k):
    if k==0 or k==n:
        return 1             #2
    p1 = p2 = p3 = 1
    for i in range(1,n+1):
        p1*=i                #3n
    for i in range(1,k+1):
        p2*=i                #3k
    for i in range(1,n-k+1):
        p3*=i                #3(n-k)
    return p1/(p2*p3)        #2 6n+7
    
#Varianta eficienta

def combinari_Iterativ2(n,k):
    if k==0 or k==n:
        return 1
    c=1
    for i in range(k+1,n+1):
        c=c*i/(n+1-i)
    return c
print(combinari_Iterativ2(4,2))