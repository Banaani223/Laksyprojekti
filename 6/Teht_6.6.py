import math

def hinta_per_neliosentti(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = sade ** 2 * math.pi
    return hinta / pinta_ala

pizza1 = int(input("Anna pizzan halkaisija (cm): "))
pizza1e = int(input("Anna pizzan hinta: "))

pizza2 = int(input("Anna toisen pizzan halkaisija (cm): "))
pizza2e = int(input("Anna toisen pizzan hinta: "))

hinta1 = hinta_per_neliosentti(pizza1, pizza1e)
hinta2 = hinta_per_neliosentti(pizza2, pizza2e)

if hinta1 < hinta2:
    print("Ensimmäinen pizza on halvempi")

elif hinta1 > hinta2:
    print("Toinen pizza on halvempi")

else:
    print("Pizzat ovat samanhintaisia")