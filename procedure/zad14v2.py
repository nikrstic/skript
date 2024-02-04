L1=["adam","pera","branko","laza","mika","aleksa","asan"]
L=[6,4,6,9,10,6,6]
parovi=list(zip(L,L1))
parovi.sort(key=lambda x: ( -x[0], x[1]))
print(parovi)
