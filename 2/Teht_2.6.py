import random

koodi1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
koodi2 = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi: {koodi1}")
print(f"Nelinumeroinen koodi: {koodi2}")