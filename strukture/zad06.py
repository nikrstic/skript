import random

M=10
L=[0]*M
for i in range(1,M):
        L[i]=i/M
L1=[0]*M
def uniformna():
    a=random.random()
    b=random.random()
    x=random.uniform(a,b)    
    sum=0
    return x
N=10000
for i in range(0,N):
    x = uniformna()
    for j in range(M-1,-1,-1):
         if x>L[j]:
              L1[j]+=1
              break

print(L1)