import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True,
         collation='utf8mb4_general_ci'
         )

koodi = input("Anna ICAO-koodi, esim. 00A: ")

sql = f"select name, municipality from airport where ident = '{koodi}'"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"Lentokentän nimi: {rivi[0]}")
    print(f"Sijaintikunta: {rivi[1]}")
