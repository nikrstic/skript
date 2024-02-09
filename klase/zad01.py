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

a = Objekat(1, 2)
b = Objekat(31, 2)
c = Objekat(11, 2)

a.X=5
a.Y = 3

print(a)
print(Objekat.ukupno_poziva())

