import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

sorgu1 ="""     
    create table Ders(id integer primary key autoincrement,
                    DersAdi text, Hocaid integer)
    """

result = cursor.execute(sorgu1)

print(result.fetchone())

sorgu2 = "select * from Ders"

result = cursor.execute(sorgu2)
print(result.fetchone())

sorgu3 = "insert into Ders(DersAdi , Hocaid)" \
          "values (\"Python\", 1)"

#print(sorgu3)

cursor.execute(sorgu3)

result = cursor.execute(sorgu2)
print(result.fetchone())

data = [("Matematik", 2),("Edebiyat", 3), ("Fizik",4)]

sorgu4 = "insert into Ders(Dersadi, Hocaid) values(?, ?)"
cursor.executemany(sorgu4 , data)

result = cursor.execute(sorgu2)

#print(result.fetchall())

s = "Tablo Icerigi"

"""print(f"{s:>15}")

for out in result.fetchall():
    print(out)"""

cursor.executescript("""
    insert into Ders(Dersadi, Hocaid) values("Fen",5);
    insert into Ders(Dersadi, Hocaid) values("Cebir",6);
    insert into Ders(Dersadi, Hocaid) values("Analiz",7);
    select * from Ders
    """)



for line in result.fetchall():
    print(line)
