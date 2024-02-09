class Ucenik:
    def __init__(self,ime,prezime):
        self._ime=ime
        self._prezime=prezime
    def poruka(self):
        return f"ja sam {self._ime} {self._prezime}"
a=Ucenik("nikola","krstic")
print(a.poruka())
b=a
print(b.poruka())
del b
