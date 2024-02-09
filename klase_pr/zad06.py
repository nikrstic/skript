a=[1,2,3,4,5]
it=iter(a)
print(type(a),type(it))

for _ in range(5):
    print(next(it), end="\n")

class EvenIter:
    def __init__(self,L):
        self.L=L
        self.idx=0
    
    def __iter__(self):
        return self
    def __next__(self):
        while self.idx<len(self.L) and self.L[self.idx] % 2 != 0:
            self.idx+=1
        if self.idx < len(self.L):
            val=self.L[self.idx]
            self.idx+=1
            return val
        else:
            raise StopIteration

print('parni: ')
for x in EvenIter([1,2,3,4,5,6,7]):
    print(x,end='\n')

    
def stepeniDvojke(num):
    for i in range(num):
        yield 2 ** i

for i in stepeniDvojke(10):
    print(i,end=' ')
print()