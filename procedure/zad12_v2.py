L=[41,32,53,34,25,16,54]
aritmeticka_sredina= [(L[x]+L[x+1])/2  for x in range(0,len(L)-1)]
print(max(aritmeticka_sredina))