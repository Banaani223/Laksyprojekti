def parittomat(numero):
    parilliset = []
    for luku in numero:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parilliset = parittomat(luvut)

print(luvut)
print(parilliset)