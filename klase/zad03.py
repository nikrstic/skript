class UnionSet:
    def __init__(self,n):
        self._n=n
        self._sets=[{i} for i in range(n)]
    
