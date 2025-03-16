class BankaHesabi:
    def __init__(self,hesap_sahibi, bakiye):
        self.hesap_sahibi = hesap_sahibi
        self.__bakiye = bakiye

    def para_cek(self,miktar):
        if miktar > self.__bakiye:
            print("Yetersiz bakiye")
        else:
            self.__bakiye = self.__bakiye - miktar
            print(f"{miktar} Tl çekildi. Kalan bakiye : {self.__bakiye - miktar}")

    def bakiye_goruntule(self):
        print(f"Bakiye miktari : {self.__bakiye}")
hesap = BankaHesabi("Şimşek",10000000)
print(f"{hesap.hesap_sahibi} icin hesap oluşturuldu")
hesap.bakiye_goruntule()

hesap.para_cek(200)
hesap.bakiye_goruntule()







