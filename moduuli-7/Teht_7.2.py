nimet = set ()
while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi arvo")
    nimet.add(nimi)
print(nimet)
