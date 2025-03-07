def cmmdc(a,b):
    a = abs(a)
    b = abs(b)
    if a*b == 0:
        return a+b
    
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

if __name__ == "__main__":
    print(cmmdc(21, 35))