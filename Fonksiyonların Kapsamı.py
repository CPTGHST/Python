#Fonksiyonların Kapsamı Global Kapsam , Local Kapsam ve Enclosure Kapsamı

degisken = 10 #Global Kapsam
liste = []

def test():
    degisken=20 #Local Kapsam
    liste.append(10) #Enclosure Kapsam
    print(f"Test1 fonksiyonu {degisken}")
    def test2():
        degisken = 100
        liste.append(20) #Enclosure Kapsam
        print(f"Test2 fonksiyonu {degisken}")
    test2()
test()
print(f"Global Test3 fonksiyonu {degisken}")
print(f"Global liste {liste}")







