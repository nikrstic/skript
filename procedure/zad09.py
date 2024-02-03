m=int(input("m: "))
n=int(input("n: "))
if(m>n):
    m,n=n,m
# n je vece 
i=m
for i in range(m,0,-1):
    if(n%i==0 and m%i==0):
        print(i)
        break
