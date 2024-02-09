import math
class Objekat:
    calls_getter = 0
    calls_setter = 0

    def __init__(self, _x, _y):
        self._x = _x
        self._y = _y

    @property
    def X(self):
        Objekat.calls_getter += 1
        return self._x

    @property
    def Y(self):
        Objekat.calls_getter += 1
        return self._y

    @X.setter
    def X(self, _x):
        Objekat.calls_setter += 1
        self._x = _x

    @Y.setter
    def Y(self, _y):
        self.y = _y
        Objekat.calls_setter += 1
    @classmethod
    def inkrements(cls):
        calls_setter+=1
    @classmethod
    def ukupno_poziva(cls):
        return cls.calls_getter + cls.calls_setter

    def __str__(self):
        return f"ovo je objekat koordinata x: {self._x}, y:{self._y}"
class Krug(Objekat):
    def  __init__ (self,x,y,r):
        super().__init__(x,y)
        self._r=r
    @property
    def R(self):
        Objekat.calls_setter+=1
        return self._r
    @staticmethod
    def float_R():
        return Objekat.R   
    def povrsina(self):
        return math.pi * self._r*self._r
a=Krug(3,4,3)

print(a.povrsina())