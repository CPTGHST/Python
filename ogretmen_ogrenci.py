import json
import sqlite3


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

with open("ogretmen.json", "r", encoding="utf-8") as fd:
    ogretmen = json.load(fd)

with open("ogrenci.json", "r", encoding="utf-8") as fd:
    ogrenci = json.load(fd)

#print(ogrenci[0]["isim"])
#print(ogretmen[0]["ders"])

ogretmen_table_create = """create table if not exists Ogretmen(id integer primary key autoincrement,
                                              isim text,
                                              soyisim text,
                                              ders text,
                                              sinif text)"""

cursor.execute(ogretmen_table_create)

ogrenci_table_create = """create table if not exists Ogrenci(id integer primary key autoincrement,
                                              isim text,
                                              soyisim text,
                                              yas integer,
                                              okul_numarasi integer,
                                              sinif text
                                              )"""

cursor.execute(ogrenci_table_create)

ogrenci_listesi = []
for ogr in ogrenci:
    print(ogr)
    ogrenci_listesi.append(tuple([ogr["isim"],
                                 ogr["soyisim"],
                                 ogr["yas"],
                                 ogr["okul_numarasi"],
                                 ogr["sinif"]
                                 ]))
print(ogrenci_listesi)
ogrenci_veri_ekle = """insert into Ogrenci(isim,
                                         soyisim,
                                         yas,
                                         okul_numarasi ,
                                         sinif) values (?,?,?,?,?)"""

cursor.executemany(ogrenci_veri_ekle,ogrenci_listesi)

result = cursor.execute("select * from Ogrenci")
print(result.fetchone())

ogretmen_listesi = []

for ogr in ogretmen:
    ogretmen_listesi.append(tuple([
        ogr["isim"],
        ogr["soyisim"],
        ogr["ders"],
        ogr["sinif"]
    ]))

print(ogretmen_listesi[0])

ogretmen_veri_ekle = """insert into Ogretmen(isim,
                                         soyisim,
                                         ders,
                                         sinif) values (?,?,?,?)"""

cursor.executemany(ogretmen_veri_ekle,ogretmen_listesi)

result = cursor.execute("select * from Ogrenci")
print(f"Ogrenci : {result.fetchone()}")