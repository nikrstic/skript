
import random
def unutar_kruga(x,y):
    rastojanje_od_centra=(x**2+y**2)**1/2
    if (rastojanje_od_centra<=0.5):
        return True
    else:
        return False
N=100000
broj_unutar=0
for _ in range (1,N):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    broj_unutar+=unutar_kruga(x,y)
print(4*broj_unutar/N)