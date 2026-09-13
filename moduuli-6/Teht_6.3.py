def muunnelma(gallonat):
    #gallona = 3.785
    # litra =  0.264

    litrat = gallonat * 3.785
    return litrat


while True:
    syote = int(input("Anna gallonat: "))
    if syote < 0:
        break
    tulos = muunnelma(syote)
    print(tulos)
