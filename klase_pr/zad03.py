class Mamal:
    def __init__ (self, name="Noname", species="Sisar"):
        self._name=name
        self._species=species
    def print_message(self):
        print(f"zdravo ja se zovem {self._name} i ja sam {self._species}")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,n):
        self._name=n
    @name.deleter
    def name(self):
        del self._name
    @property
    def species(self,s):
        self._species=s
    @species.setter
    def species(self,s):
        self._species=s
    @staticmethod
    def greetings():
        print('greeting from animal')
    count=0
    @classmethod
    def incr(cls):
        cls.count+=1
class Hourse(Mamal):
    pass
m=Mamal()
m.name="Sarac"
m.species="Konj"
m.print_message()
m1=Mamal(name='Sarac',species='Konj')
m1.print_message()
m1=m
m.name="xx"
m1.print_message()
Mamal.greetings()
m.greetings()
m.incr()
print(Mamal.count)
print(Hourse().count)