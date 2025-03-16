# try except
from sys import excepthook

"""a = input("1. değeri girin:")
b = input("2. değeri girin:")
try:
    print(a / b)
except:
    if a.isdigit() and b.isdigit():
        print("Hata ile karşılaşıldı")
        print(int(a) / int(b))
    else:
        print("Tam sayı giriniz!")
finally:
    print("Finally çalıştı")"""

#Sifira bolme hatasi
"""try :
    a = int(input("1.değer:"))
    b = int(input("2.değer:"))

    print(a/b)

except ZeroDivisionError as e:
    print("Sifira bolme hatasi",e)
except ValueError as e:
    print("Hatali değer",e)
except Exception as e:
    print("Hata",e)"""

"""try:
    sonuc = 4 + "5"
except TypeError as e:
    print("Tip hatasi:",e)"""

