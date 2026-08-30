alkuluku = int(input("Anna luku: "))
for i in range(2, alkuluku):
    if alkuluku % i == 0:
        print("Luku ei ole alkuluku")
        break
else: print("Luku on alkuluku")