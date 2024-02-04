M=int(input("unesite broj ljudi: "))

suma=1.0
for i in range(M):
    suma*=(365-i)/365
    
print(1-suma)