import random

N=10000
def bacanje_kockica():
    prva=random.randint(1,6)
    druga=random.randint(1,6)
    treca=random.randint(1,6)
    s=prva+druga+treca
    return s
niz=[0 for _ in range(19-3)]
for x in range (3,19):
    print (f"{x}", end=" " )
print()
for i in range (1,N):
    niz[bacanje_kockica()-3]+=1
print(niz)