L=[1,2,3,4,5,7,8]
def suffle(L):
    L1 = [x for x in L if (x%2==0)]
    L1.extend( [x for x in L if x%2==1])
    return L1
rezultat=suffle(L)
print(rezultat)