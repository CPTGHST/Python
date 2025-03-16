# Lambda Fonksiyonu

"""def toplama(a,b):
     return a + b
toplama2 = lambda x, y : x + y

print(toplama(1,2))
print(toplama2(1,2))"""
from turtledemo.penrose import start

# Map Fonksiyonu

"""sayilar = [1, 2, 3, 4]
m= map(lambda x : x**2,sayilar)
print(list(m))"""

# Zip Fonksiyonu

"""isimler = ["Ali", "Veli", "Ayşe"]
yaslar = [25, 30, 22]
birlesim = list(zip(isimler, yaslar))
print(birlesim)"""

# Enumerate Fonksiyonu

"""meyveler = ["elma","armut","muz"]

print(enumerate(meyveler , start = 10))

for index, meyve in enumerate(meyveler):
    print(f"index:{index} meyve : {meyve}")"""

# Filter Fonksiyonu

"""sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sayılar = lambda x : x % 2 == 0

liste = list(filter(cift_sayılar, sayilar))
print(liste)"""

#Q3-Çift Sayıları Bulma (filter ve lambda)

"""sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sayılar = lambda x : x % 2 == 0

liste = list(filter(cift_sayılar, sayilar))
print(liste)"""

#Q2-İki Listeyi Birleştirme (zip ve lambda)

"""liste1 = [2, 4, 6]
liste2 = [3, 5, 7]

carpim = lambda x,y: x*y

liste = []
for sayi1,sayi2 in zip(liste1,liste2):
    liste.append(carpim(sayi1,sayi2))

print(liste)"""

#Q3-Listedeki Uzun Kelimeleri Bulma (filter ve lambda)

"""kelimeler = ["elma", "armut", "portakal", "kavun", "kiraz", "üzüm"]

uzunkelimeler = lambda x: len(x) >= 5
liste = list(filter(uzunkelimeler, kelimeler))
print(liste)"""

#Q4-Listedeki Elemanlara İndeks Atama (enumerate)

"""kelimeler = ["Python", "Java", "C++", "JavaScript"]
print(enumerate(kelimeler , start = 10))

for i, kelime in enumerate(kelimeler,start=10):
    print(f" i:{i} kelime : {kelime}")"""

#Q5-Listedeki Sayıları Artırma (map ve lambda)

"""sayilar = [1, 4, 7, 10]

m= map(lambda x : x+1,sayilar)
print(list(m))"""

#Algoritma Soruları

#Q1-listedeki ortalama değerden büyük olan tüm sayıları bulan bir fonksiyon yazın.filter() ve lambda kullanarak bu işlemi gerçekleştirin. (Filter ve Lambda)

"""sayilar = [3, 7, 10, 12, 15, 22, 9, 2]

ortalama = sum(sayilar) / len(sayilar)

liste =list(filter(lambda x : x > ortalama, sayilar))
print(liste)"""

#Q2-İki farklı öğrenci grubunu içeren iki liste verildiğinde, her iki listedeki öğrencileri zip() kullanarak eşleştirin. Öğrenciler isme ve yaşa göre birleştirilecek.

"""ogrenci_isimleri = ["Ahmet", "Ayşe", "Mehmet", "Fatma"]
ogrenci_yaslari = [15, 16, 14, 17]

birlesim = list(zip(ogrenci_isimleri,ogrenci_yaslari))
print(birlesim)"""

#Q3- Fibonacci Dizisi Oluşturma (lambda ve map) [Fn = Fn-1 + Fn-2] !!!!!Eksik Çözüm doğrusu yazılacak

"""def fibonacci(n):
    # Fibonacci dizisini oluşturmakiçin bir liste
    fib = [0,1]
    #Fibonacci dizisinin N elemanını hesapla
    list(map(lambda _:fib.append(fib[-1] + fib[-2]), range(2,n)))
    return fib[:n]
n = 7
print(fibonacci(n))"""

#Q4-Bir kelime listesindeki sadece çift indekslerde bulunan kelimeleri döndüren bir fonksiyon yazın.enumerate() ve lambda kullanarak çözümü gerçekleştirin.

"""kelimeler =["elma", "armut", "kiraz", "muz", "kavun", "üzüm" ]

liste = list(filter(lambda a: a[0] % 2 == 0 , enumerate(kelimeler)))
print(liste)"""

#Q5-İki sayı listesindeki elemanları zip() ile birleştirip, her iki listedeki karşılıklı elemanların toplamını döndüren bir fonksiyon yazın. map() ve lambda kullanarak toplamları hesaplayın.

"""liste1 = [1, 2, 3, 4]
liste2 = [10, 20, 30, 40]

toplama = list(map(lambda x: x[0]+x[1], zip(liste1 , liste2)))

print(toplama)"""




