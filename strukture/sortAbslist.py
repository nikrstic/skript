
L=[1,2,3,-23,-54,65,2,-76]
L.sort(reverse=True, key=lambda x:(x**2)**1/2)
L.sort(key=abs)
print(L)