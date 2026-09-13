hemoglobiini = int(input("Anna hemoglobiinitasosi: "))
sukupuoli = input("Anna sukupuoli (nainen/mies): ").lower()

if sukupuoli == "nainen":
    min_normaali = 117
    max_normaali = 175
elif sukupuoli == "mies":
    min_normaali = 134
    max_normaali = 195
else:
    print("Virheellinen sukupuoli")
    exit()

if min_normaali <= hemoglobiini <= max_normaali:
    print("Hemoglobiinitasosi on normaali")
elif hemoglobiini > max_normaali:
    print("Hemoglobiinitasosi on liian korkea")
elif hemoglobiini < min_normaali:
    print("Hemoglobiinitasosi on liian matala")
