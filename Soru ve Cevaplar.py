#Q1-Kullanıcıdan alınan değerin tek mi çift mi olduğunu belirleme

"""1. Başla.
2. Yaz " Sayı giriniz " ; oku a ;                                   # mod = %
3. Eğer a mod 2 = 0 : yaz " Girilen sayı çifttir " ;
3. Değilse Eğer " Girilen sayı tektir " ;
4. Bitir.

sayi = input("Sayı giriniz : ")
print(sayi,type(sayi))
if sayi[0] == "-":
    sayi = int(sayi[1:])

if sayi.isdigit():
    sayi = int(sayi)

print(sayi ,type(sayi))

if sayi % 2 == 0:
    print("Girilen sayı çifttir")
else:
    print("Girilen sayı tektir")"""


#Q2-Kullanicadan alınan sayının tersini alan kodu yazınız.Örnek: Girdi: -1 Cikti: 1 Girdi: 1 Cikti: -1

"""print("Sayi giriniz :")
sayi = int(input())

if sayi > 0:
    print("Sayi pozitiftir , tersi:", -sayi)
elif sayi < 0 :
    print("Sayi negatiftir , tersi:", -sayi)
else:
    print("Sifir girdiniz")"""

#Q3-Kullanicidan bir vize ve bir final notu isteyiniz.Eger vize ve final notu 0 ile 100 arasinda degilse ekrana hata mesaji veriniz.Eger 0 ile 100 arasinda ise not ortalamasinin %40 ni ile final notunun %60 nin toplami olarak hesaplayip ekranda yazdiriniz. Ardindan not ortalamasini asagidaki kurala gore hesaplayip ekrana yazdiriniz.

"""vize_notu = int(input("Vize notunuzu giriniz :"))
final_notu = int(input("Final notunuzu giriniz :"))

if (vize_notu < 0 or vize_notu > 100) or \
        (final_notu < 0 or final_notu > 100) :
    print("Hatali giriş yaptınız")
else:
    ortalama = vize_notu * 0.4 + final_notu * 0.60
    print(ortalama)

if  0<= ortalama < 60:
    print("Not: FF")
elif 60 <= ortalama < 70 :
    print("Not : DD")
elif 70 <= ortalama < 80 :
    print("Not : CC")
elif 80 <= ortalama < 90 :
    print("Not : BB")
elif 90<= ortalama <= 100 :
    print("Not : AA")"""

#Q4-Kullanicidan dikdortgen kare secmesini isteyiniz. Ardindan secim yanlissa hata mesaji veriniz. Uygun sekilde secim yapilmissa secilen sekle gore kenar uzunluklarini isteyiniz ardindan alan ve cevre degerlerini hesaplayiniz.

"""Kenar1 = input(("İlk kenarı giriniz : "))

Kenar2 = input(("İkinci kenarı giriniz : "))

Çevre == 0
Alan == 0

if Kenar1 == Kenar2 :

    Çevre == Kenar1 * 4
    Alan == Kenar1
    print(Çevre, Alan)
else :
    Çevre == 2 * (Kenar1 + Kenar2)
    Alan == Kenar1 ^ 2
    print(Çevre, Alan)"""

#Q5-Kullanicidan iki sayi isteyiniz sonrasinda yapilmak istenilen islemi isteyiniz (carpma,bolme,toplama, cikarma). Sonrasinda islemi yapip sonucu ekrana yazdiriniz

"""num1 = int(input("Bir sayı giriniz :"))
num2 = int(input("Bir sayı giriniz"))
operation = input("Bir işlem giriniz")

if operation == "+":
    print(f"İşlem sonucu : {num1 + num2}")

if operation == "-":
    print(f"İşlem sonucu : {num1 - num2}")

if operation == "*":
    print(f"İşlem sonucu : {num1 * num2}")

if operation == "/":
    print(f"İşlem sonucu : {num1 / num2}")"""

#Q6-Bir 4 haneli pin kodu belirleyiniz. Bu pin kodunu uygulamaniza kisiyi dogrulamakta kullanmak icin kullancaksiniz.Kullanici 3 kez yanlis pin girdiginde uyari mesaji vererek uygulamayi sonlandirir. Basarili giriste ise "Giris dogrulandi" seklinde ekrana bildirim versin.

"""giris_basarılı = False
pin = "1234"

for i in range(3):
    girilen_pin = input(("Pin giriniz : "))

if girilen_pin == pin :
    giris_basarılı = True
    break

else:
    print("Hatalı giriş yaptınız")

if giris_basarılı:
    print("Giris tamamlandı") """

#Q7- Kullanicidan bir sayi girilmesi istinilsin ekran girilen sayiya kadar olan sayilar yazdirilsin.

"""num1 = int(input("Bir sayı giriniz :"))
for i in range(num1):
    print(i)"""

#Q8 - Kullanicidan alt limit ust limit ve artis miktari istenilsin.Ekran alt limitten baslayarak artis miktari kadar artirarak ust limite kadar sayilar ekrana yazdirilsin.

"""alt_limit = int(input("Alt limit giriniz :"))
ust_limit = int(input("Üst limit giriniz :"))
artis_miktari = int(input("Artış miktari giriniz :"))

for i in range(alt_limit , ust_limit + 1 , artis_miktari) :"""
#Q9 - Kullanicidan alt limit ve ust limit alinsin ve aradaki sayilarin toplami hesaplansin.

"""alt_limit = int(input("Alt limit giriniz :"))
ust_limit = int(input("Üst limit giriniz :"))

toplam = sum(range(alt_limit, ust_limit + 1))

print(f"{alt_limit} ile {ust_limit} arasındaki sayıların toplamı: {toplam}")"""

#Q10-Girilen sayinin faktoriyelini hesaplayan kodu yaziniz eger deger sifirdan kucukse hata mesaji verin

"""sayi = int(input("Sayı giriniz :"))
sonuc = 1
for i in range(1,sayi+1):
    sonuc= sonuc * i
print(f"Faktoriyel = {sonuc}")"""

#Q11-Girilen sayinin tum pozitif bolenlerini bulunuz.

"""sayi = int(input("Sayı giriniz :"))

for bolen in range(2,sayi+1):
    if sayi % bolen == 0:
        print(bolen)"""
#Q12-Girilen sayinin asal olup olmadigini kontrol edip asalsa "Bu bir asal sayidir" degilse "Asal sayi degildir" seklinde ekrana mesaj yaziniz.

#Q13-Girilen metnin tersten ve duzden birbirine esit olup olmadigini kontrol eden kodu yaziniz. Ornek: abcba == polindromdur deded == polindromdur dead != polindrom degildir

"""def polindrom_kontrol(text):
    if text == text[::-1]:
        print("Polindromdur")
    else:
    print("Polindrom değildir")
polindrom_kontrol(input("Metni giriniz :"))"""

#Q14- a = 2 b = 3 c = 4 icin girilen sayi icin denklemi hesaplayan fonksiyonu yaziniz

#Q15-Girilen sayinin rakamlari toplamini bulan programini bulan kodu yaziniz.

"""sayi = int(input("Değer giriniz"))

x = []
while sayi > 0:
    x.append(sayi % 10)
    sayi = sayi // 10

x.reverse()
print(x,sum(x))"""

"""def toplama(*parametreler):
    print(sum(parametreler))
    print(parametreler[0],parametreler[1],len(parametreler))

toplama(1,2,3,4)
toplama(1,2,3)
toplama(12,12)

def kisi_bilgisi(**parametre):
    print(parametre)
    print(parametre["isim"], parametre["yas"], parametre["ulke"])

kisi_bilgisi(isim = "Ali", yas = 30,ulke = "TR")"""

#1.Hafta Genel Tekrar Soruları

#Q1-Soru: Bir liste içinde tekrar eden ilk sayıyı bulun.
#İpucu: set yapısını kullanarak daha hızlı çözüm bulunabilir.
#Örnek: [2, 1, 2, 3] girdisi için sonuç 2 olmalı.

"""liste=[2, 1, 2, 3]
for i in set(liste):
    if liste.count(i) > 1:
        print(i)
        break"""

#Q2-Soru: İki kelimenin anagram olup olmadığını kontrol eden bir fonksiyon yazın.
#İpucu: Counter veya sorted() kullanılabilir.
#Örnek: ("listen", "silent") girdisi için sonuç True olmalı.

"""kelime1,kelime2 = "listen","silent"

if set(kelime1) == set(kelime2)
    print("Anagram")"""

#Q3-Soru: İki liste verildiğinde, bunları dönüşümlü olarak birleştiren bir fonksiyon yazın.
#İpucu: zip() fonksiyonu kullanılabilir.
#Örnek: ([1, 2, 3], [4, 5, 6]) girdisi için sonuç [1, 4, 2, 5, 3, 6] olmalı.

"""liste1=[1, 2, 3]
liste2=[4, 5, 6]

liste =[]
for i,j in zip(liste1,liste2):
    liste.append(i)
    liste.append(j)

print(liste)"""

#Q4-Soru: Bir dizide ardışık elemanlardan oluşan en büyük toplamı bulan bir fonksiyon yazın.
#İpucu: Kadane algoritması kullanılabilir.
#Örnek: [−2, 1, −3, 4, −1, 2, 1, −5, 4] girdisi için sonuç 6 olmalı.

"""dizi = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_toplam = 0
for i in range(len(dizi)):
    for j in range(i+1,len(dizi)+1):
        print(dizi[i:j])
        if max_toplam < sum(dizi[i:j]):
            max_toplam = sum(dizi[i:j])

print(max_toplam)"""




