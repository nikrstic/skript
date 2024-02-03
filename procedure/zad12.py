L=[41,32,53,34,25,16,54]
max=(L[0]+L[1])/2
def aritmeticka(a,b):
    return (a+b)/2
for i in range(0,len(L)-1):
    if aritmeticka(L[i],L[i+1]) > max:
        max = aritmeticka(L[i],L[i+1])
print(max)