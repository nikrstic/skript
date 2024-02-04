from datetime import datetime,timedelta
sada=datetime.now()
print(sada)

dani=("ponedeljak", "utorak","sreda","cetvrtak","petak","subota","nedelja")
print(dani[sada.isoweekday()])
for i in range (1,7):
    sada+=timedelta(days=1)
    print(dani[sada.isoweekday()-1])