import random

L={x:0 for x in range(1,37)}

def eksperiment():
    n=random.randint(1,6)
    sum=0
    for i in range(1,n+1):
        sum+= random.randint(1,6)
    return sum
for a in range(100000):
    suma=eksperiment()
    L[suma]+=1
print(L)