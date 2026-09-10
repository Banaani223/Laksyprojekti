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

koodi = input("Anna maakoodi, esim. FI: ")

sql = f"select type, count(*) from airportwhere iso_country = '{koodi}' group by type"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(rivi)