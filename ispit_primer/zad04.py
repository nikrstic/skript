
class Razlomak():
    def __init__ (self, brojilac, imenilac):
        if imenilac==0:
            raise ValueError("ne moze nula")
        elif imenilac<0:
            brojilac,imenilac=-brojilac,-imenilac
        self.brojilac=brojilac
        self.imenilac=imenilac
        self.skrati()
    def skrati(self):
        a,b=abs(self.brojilac),abs(self.imenilac)
        if a<b:
            a,b=b,a
        while True:
            r=a%b
            a,b=b,r
            if r==0:
                break
        self.brojilac//=a
        self.imenilac//=a
    def __add__ (self,other):
        if type(other) == Razlomak:
            br=self.brojilac*other.imenilac+self.imenilac*other.brojilac
            im=self.imenilac*other.imenilac
            return Razlomak(br,im)
        if type(other) == int:
            return self+Razlomak(other,1)
        else:
            raise ValueError("greska")
    def __str__(self):
        return f"{self.brojilac}/{self.imenilac}"
a=Razlomak(3,4)
b=Razlomak(2,8)
c=a+b
print(c)