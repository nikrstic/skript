materijali=80
energenti=100
cena_rada=800
sati_rada=7
taksa=20
def cena_rada(materijali, energenti,cena_rada,sati_rada):
    ukupna_cena=(materijali+energenti+cena_rada*sati_rada)*(100+(taksa/100))
    return ukupna_cena
