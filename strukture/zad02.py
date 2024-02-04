import random
N=10000
vrednosti={}
for i in range(0,13):
    vrednosti[i]=0
provera1=0
for _ in range(1,N+1):
    a=random.randint(1,6)
    b=random.randint(1,6)
    vrednosti[a+b]+=1
    provera1+=1
print(provera1)
print(vrednosti)
provera=0
for i in range (2,13):
    print(f"{i}:{vrednosti[i]/N*100}")
    provera+=vrednosti[i]/N*100

print(provera)