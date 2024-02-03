x = int(input("Unesite x: "))
y = int(input("Unesite y: "))
z = int(input("unesite z: "))
q = int(input("unesite q: "))
vremeSekunde=x*3600+y*60+z+q
sati,ostatak = divmod(vremeSekunde,3600)
minuti, ostatak=divmod(ostatak,60)
print(f"{sati}:{minuti}:{ostatak}")