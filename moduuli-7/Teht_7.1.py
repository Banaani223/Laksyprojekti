kuukaudet = {"1":"Joulukuu",
             "2":"Tammikuu",
             "3":"Helmikuu",
             "4":"Maaliskuu",
             "5":"Huhtikuu",
             "6":"Toukokuu",
             "7":"Kesäkuu",
             "8":"Heinäkuu",
             "9":"Elokuu",
             "10":"Syyskuu",
             "11":"Lokakuu",
             "12":"Marraskuu",}

vuodenajat = ("talvi", "talvi",  "talvi",
              "kevät", "kevät", "kevät",
              "kesä", "kesä", "kesä",
              "syksy", "syksy", "syksy")


kuukausi = input("Anna kuukausi (1-12): ")
if kuukausi in kuukaudet:
    print (f"Kuukausi {kuukausi} on {kuukaudet[kuukausi]}.")
    indeksi = int(kuukausi) - 1
    print(f"Vuodenaika on {vuodenajat[indeksi]}.")
