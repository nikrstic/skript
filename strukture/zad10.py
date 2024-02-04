
with open("strukture/smsSpam.txt", "r") as f,open("strukture/ham.txt", "w") as f1,open("strukture/spam.txt","w") as f2:    
    while True:
        linija=f.readline()
        if not f.readline():
                break
        if linija.split()[0]=="ham":
             f1.write(linija)
        if linija.split()[0]=="spam":
             f2.write(linija)