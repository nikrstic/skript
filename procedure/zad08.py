cena=20000
k=int(input("k: "))
for i in range (1,k+1):
    if k <= 5:
        cena*=0.85
    else:
        cena*=0.9
print(cena)