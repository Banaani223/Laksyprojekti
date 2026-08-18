pituus = float(input("Anna suorakulmion pituus: "))
leveys = float(input("Anna suorakulmion leveys: "))

pinta_ala = pituus * leveys
piiri = pituus * 2 + leveys * 2

print (f"Suorakulmion pinta-ala on {pinta_ala:.2f} ja piiri {piiri:.2f}")