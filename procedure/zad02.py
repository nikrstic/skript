vreme=int(input("unesi sate: "))
def odredi_doba(vreme):
    if 6<=vreme<=10:
        print("jutro")
    elif 10<vreme<=18:
        print("dan")
    elif 18<vreme<22:
        print("vece")
    else:
        print("noc")

odredi_doba(vreme)