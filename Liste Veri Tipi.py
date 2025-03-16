liste = [1,2,3]
print(liste)
print(type(liste))
liste = [1,1,2,3]
print(liste)
liste = [1,2,"muhammet", 1.23]
print(liste)
print(f"liste uzunulugu = {len(liste)}")
print(f"liste elemanina erisim : {liste[0]}")
print(f"listenin belirli elemanlarina erisim : {liste[0:3]}")

liste = [10, 20, 30]

liste.append(40)
print(f"Eleman ekleme : {liste}")

liste.insert(0,50)
print(f"0. indise eklendi : {liste}")

liste2 = [100,200,300]
liste.extend(liste2)

print(f"extend sonrasi  :{liste} ")

liste3 = [400,500]
liste.append(liste3)
print(f"liste ekleme : {liste}")

liste = [10, 20, 30, 40,20, 50]

#20 degerini siler
liste.remove(20)
print(liste)

#Son elemani siler
liste.pop()
print(liste)

#0. indisdeki degeri siler
liste.pop(0)
print(liste)

#0. indisi siler
del liste[0]
print(liste)

#listeyi temizler
#liste.clear()
print(liste)

#indeks degerini ogrenme
print(liste.index(40))

liste = [10, 20, 30, 40,20, 50]
print(liste.count(20))
liste.sort()
print(liste)
liste = [10, 20, 30, 40,20, 50,-1]
liste.reverse()
print(liste)
liste = ["Python ", "programlama"]
print(' '.join(liste))

#Liste elemanini guncelleme
liste[0] = "deneme"
print(liste)
liste = [10, 20, 30, 40,20, 50]
print(set(liste))
print(liste[:4:2])