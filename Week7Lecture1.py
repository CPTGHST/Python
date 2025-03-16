import sqlite3
import os

print(os.getcwd())
conn = sqlite3.connect('kitaplar.sqlite') #Bağlanyı nesnesi
cursor = conn.cursor() #Cursor aracılığıyla sonuçları takip edebiliriz. Notepadd'deki imleç gibi çalışır

query = "select * from Kitaplar"
result = cursor.execute("select * from Kitaplar") #cursor'ı çağırmak için kullanılır
print(result.fetchone()) #1 tane sonuç getirir
print(result.fetchmany(3)) #Birden çok sonuç getirir: Bu örnekte 3 sonuç getirir
#print(result.fetchall()) #Tüm sonuçları getirir

#Tüm sonuçları tek satırda getirdiği için okunması zor
#Her sonucu tek satırda göstermesi için for döngüsü kullandık
for out in result.fetchall():
    print(out)

values_list = [('Degirmen', 'Sabahattin Ali','40 TL'),('Kayip Tanrilar Ulkesinde','Ahmet Umit','300 TL'),('Satranç','Stephan Zweig','30 TL'),('Semerkand','Zulfu Livaneli','150 TL')]

sorgu = 'insert into Kitaplar values(?,?,?)'
cursor.executemany(sorgu,values_list)

result = cursor.execute(query)

for out in result:
    print(out)

conn.commit()
conn.close()