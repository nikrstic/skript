n=155
def generisi(n):
    L=[]
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    print(L)
generisi(n)
