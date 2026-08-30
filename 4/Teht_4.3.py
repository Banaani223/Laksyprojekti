pienin = None
suurin = None
kerrat = 0
while True:
    luku = input("Anna luku (tyhjä lopettaa): ")
    if luku == "":
        break

    luku = int(luku)

    if pienin is None:
        pienin = luku
        suurin = luku

    if luku < pienin:
        pienin = luku

    if luku > suurin:
        suurin = luku

print (f"Suurin luku on {suurin}")
print (f"Pienin luku on {pienin}")