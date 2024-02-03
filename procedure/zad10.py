L=[1,2,3,4,5,6,7,8,22]
suma=0
for i in L:
    if i%2==0:
        suma+=i
print(suma)
suma_parnih=sum(x for x in L if x%2==0)
print(suma_parnih)