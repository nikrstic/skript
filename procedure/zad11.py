L=[65,43,432,54,4234,54,2,432,543]
min=L[0]
pozicija=0
for i in L:
    if i<min:
        min=i
        sacuvaj=pozicija
    pozicija+=1
print(f"pozicija:{pozicija}, broj: {sacuvaj}")