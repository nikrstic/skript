class Osoba:
    def __init__ (self, ime, prezime):
        self._ime=ime
        self._prezime=prezime
    def poruka(self):
        return f"ja sam {self._ime} {self._prezime}"
class Student(Osoba):
    def __init__ (self,ime, prezime,godina):
        super().__init__(ime,prezime)
        self._godina=godina
    def poruka_osoba(self):
        super().poruka()
    def __str__(self):
        return f"ja sam {self._ime} {self._prezime} i na faksu sam {self._godina} godina"
    
s= Student("pera", "peric",6)
s.poruka()
s.poruka_osoba()
print(s)