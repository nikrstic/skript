class Razlomak:
    def __init__(self, brojilac, imenilac):
        if imenilac==0:
            raise ValueError("ne moze nula")
        elif imenilac<0:
            brojilac,imenilac = -brojilac,-imenilac
        self.brojilac= brojilac
        self.imenilac=imenilac
    def skrati(self):
        a,b=abs(self.brojilac), abs(self.imenilac)
        if a<b:
            a,b = b,a
        while True:
            r=a%b
            a,b=b,r
            if(r==0):
                break
        self.brojilac//= a
        self.imenilac//=b
    def __add__(self,other):
        if type(other) == Razlomak:
            novi_imenilac=self.imenilac*other.brojilac+other.imenilac*self.brojilac
            novi_brojilac= self.brojilac*other.brojilac
            return Razlomak(novi_imenilac,novi_brojilac)
        if type(other) == int:
            return self+ Razlomak(other,1)
        raise ValueError("argument je pogresnog tipa")
    def __mul__(self,other):
        if type(other)==Razlomak:
            return Razlomak(self.imenilac*other.imenilac,self.brojilac*other.brojilac)
        elif type(other)==int:
            return Razlomak(self.imenilac*other,self.brojilac)
        raise ValueError("argument je pogresnog tipa")
    def __radd__ (self,other):
        return self+other
    def __rmul__ (self,other):
        return self*other
    def __substraction__ (self,other):
        return self+(-1)*other
    def __rsub__(self,other):
        return other*(-1)+self
    #def __rtruediv__(self,other):
    