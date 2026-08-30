yritys = 1
while True:
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana:")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    elif yritys == 5:
        print("Pääsy evätty")
        break
    else:
        yritys += 1
        continue