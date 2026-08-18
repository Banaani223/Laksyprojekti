luoti_grammat = 13,3
naula_luodeissa = 32
leiviskat_nauloissa = 20

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (leiviskat * 20 * 32 * 13.3 +
           naulat * 32 * 13.3 +
           luodit * 13.3)

kg = int(grammat // 1000)
g = grammat % 1000

print(f"\nMassa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {g:.2f} grammaa.")