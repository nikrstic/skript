L1=["pera","branko","laza","mika","aleksa"]
L=[4,6,9,10,6]
for i in range(0,len(L)):
    for j in range(0,len(L)):
        if(L[i]>L[j]):
            L[i],L[j]=L[j],L[i]
            L1[i],L1[j]=L1[j],L1[i]
        if(L[i]==L[j]):
            if(L1[i]<L1[j]):
                L[i],L[j]=L[j],L[i]
                L1[i],L1[j]=L1[j],L1[i]

print(L)
print(L1)