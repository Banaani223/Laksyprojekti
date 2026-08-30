import random
kuutiot = int(input("Kuinka monta kuutiota heitetään? "))

summa = 0
for kuutio in range(kuutiot):
    noppa = random.randint(1, 6)
    summa += noppa

print(summa)