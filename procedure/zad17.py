s="Dat String S"
def velikaImala(s):
    mala=0
    velika=0
    for i in s:
        if i.islower():
            mala=mala+1
        if i.isupper():
            velika=velika+1
    return velika,mala

rezultat=velikaImala(s)
print(rezultat[0])
print(rezultat[1])