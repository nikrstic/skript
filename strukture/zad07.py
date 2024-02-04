import random
L=[x for x in range (1,37)]
#print(L)
L1=[0]*36
def eksperiment(L1):
    sum=0
    n=random.randint(1,6)
    for i in range(0,n):
        a=random.randint(1,6)
        sum+=a
    return sum
for i in range(100000):
    suma=eksperiment(L1)
    L1[suma-1]+=1
L2=dict(zip(L,L1))
print(L2)