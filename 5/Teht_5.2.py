luvut = []

luku = input("Anna luku: ")

while luku != "":
    syote_numerona = int(luku)
    luvut.append(syote_numerona)
    luku = input("Anna luku: ")

luvut.sort(reverse=True)
print (luvut[:5])
