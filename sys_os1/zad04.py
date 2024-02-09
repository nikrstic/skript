import os

fd=os.open('rand.dat',os.O_RDWR|os.O_CREAT)
print(fd)
data='Tekstualni podaci: '.encode()
os.write(fd,b'\0'*10)
os.write(fd,bytes([1,2,3,4,5]))
os.close(fd)
fd=os.open('rand.dat',os.O_RDONLY)
dat=os.read(fd,100)
print(len(dat),dat)
os.close(fd)
