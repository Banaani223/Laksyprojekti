import random

luku = random.randint(1, 10)
while True:

    #print(luku)
    arvaus = (input("Arvaa luku: "))
    arvausint = int(arvaus)
    if luku > arvausint:
        print("Luku on suurempi")
    elif luku < arvausint:
        print("Luku on pienempi")
    else:
        print("Arvasit")
        break