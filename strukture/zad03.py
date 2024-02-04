from datetime import datetime,timedelta
sada=datetime.now()
print(sada)
print(sada.isoweekday())
dani=("ponedeljak", "utorak","sreda","cetvrtak","petak","subota","nedelja")
for i in range (1,7):
    sada+=timedelta(days=1)
    print(dani[sada.isoweekday()-1])