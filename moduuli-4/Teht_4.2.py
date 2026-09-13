while True:
    tuumat = int(input("Anna tuumat (negatiivinen lopettaa): "))
    sentit = tuumat * 2.54
    if tuumat < 0:
        break
    print(sentit)