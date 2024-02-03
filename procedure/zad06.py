n=int(input("unesi n"))
k=[i for i in range(3,n,3)]
for i in k:
    if((i-1)%7!=0) and ((i+1)%7!=0):
        print(i)
        