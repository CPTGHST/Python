bos_sozluk = {}
print(bos_sozluk,type(bos_sozluk))

sozluk = {1:"bir",2:["iki","4"], 3:"uc"}

print(f"Sozluk : {sozluk}")

sozluk = {(1,2):"bir ve iki"}

print(sozluk)
sozluk = {1:"bir",2:["iki","4"], 3:"uc"}
print(sozluk[1])

print(sozluk.get(0,"Kayit bulunamadi"))

sozluk[4] = "dort"
print(f"4 Eklendi : {sozluk}")
sozluk[5] = "bes"
sozluk[4] = "yeni dort"
print(f"Guncellenmis hali : {sozluk}")

del sozluk[1]
print(f"silinme islemi sonrasi : {sozluk}")

print(f"2 anahtari silindi: {sozluk.pop(2)}")

print(f"Sozluk = {sozluk}")
sozluk.popitem()
print(f"Son eleman silindi : {sozluk}")

#sozluk.clear()
print(f"Clear sonrasi : {sozluk}")

print(f"Anahtar degerleri : {sozluk.keys()}")

print(f"Anahtar degerlerine karsilik gelen degerler : {sozluk.values()} ")

print(f" items : {sozluk.items()}")

sozluk.update({3:"yeni uc", 5:"bes"})
print(sozluk)

