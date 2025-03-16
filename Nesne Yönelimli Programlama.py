"""class Araba:
    def __init__(self,marka,model):
        self.marka = marka
        self.model = model

    def bilgi_göster():
        print(f"Marka : {self.__marka}",
              f"Model : {self.__model}", sep="\n")

araba = Araba(marka="Toyota",model="Corolla")
#print(f"Marka : {araba.__marka} , Model : {araba.__model}")
araba.bilgi_göster()"""

class Canli:
    def __init__(self,isim):
        self.isim = isim
    def hareket(self):
        print(f"{self.isim} hareket ediyor")
class Hayvan(Canli):
    def __init__(self,isim,yas):
        super().__init__(isim)
        self.yas = yas

    def bilgi_göster(self):
        print(f"Isim : {self.isim}",
              f"Yas : {self.yas}", sep = "\n")

"""kedi = Hayvan("Kedi","2")
#print(kedi.isim,kedi.yas)
kedi.hareket()
kedi.bilgi_göster()"""

class Insan(Canli):
    def __init__(self,isim,cinsiyet,yas):
        super().__init__(isim)
        self.yas = yas
        self.cinsiyet = cinsiyet

    def bilgi_goster(self):
        print(f"İsim: {self.isim}",
              f"Cinsiyet : {self.cinsiyet}",
              f"Yas : {self.yas}", sep="\n")

class Calisan(Insan):
    def __init__(self,isim,cinsiyet,yas,kurum,kidem):
            super().__init__(isim,yas,cinsiyet)
            self.kurum = kurum
            self.kidem = kidem

    def bilgi_goster(self):
        print(f"İsim: {self.isim}",
              f"Cinsiyet : {self.cinsiyet}",
              f"Yas : {self.yas}",
              f"Kurum : {self.kurum}",
              f"Kidem : {self.kidem}", sep="\n")

ahmet = Calisan("ahmet","erkek","20","Microsoft","Stajyer")
ahmet.bilgi_goster()
ahmet.hareket()