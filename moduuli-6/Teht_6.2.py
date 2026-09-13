import random

def satunnaisluku(tahkot):
    luku = random.randint(1,tahkot)
    return luku

tahko = int(input("Tahko: "))
luku = 0
while luku != tahko:
    luku = satunnaisluku(tahko)
    print(luku)