temperatura = int(input("unesite temperaturu: "))
def agregatno(temperatura):
    if 0<temperatura<100:
        print("tecno")
    elif temperatura<0:
        print("cvrsto")
    else:
        print("gasovito")

agregatno(temperatura)