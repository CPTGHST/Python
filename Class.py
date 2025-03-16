class Araba:
    ulke = "Turkiye"
    marka = "Toyota"
    model = "Coralla"
    renk = "Mavi"
    def __init__(self, marka="Toyota", model="Corolla", renk="Mavi"):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.hizi = 0

    def calistir(self):
        print(f"{self.marka} {self.model} {self.renk} calisiyor")

    def hizlan(self,hiz):
        self.hizi = self.hizi + hiz
        print(f"Simdiki hiz :{self.hizi}")

    def hiz(self):
        return self.hizi

    def bilgi_goster(self):
        print(f"Marka:{self.marka}",
              f"Model:{self.model}",
              f"Renk:{self.renk}",
              f"Ulke:{self.ulke}",sep='\n')
araba = Araba()
#print("Marka : {} Model : {} Renk : {}".format(araba.marka,araba.model,araba.renk))
araba.bilgi_goster()

araba2 = Araba("Volvo", "Xc90", "Siyah")
araba2.bilgi_goster()
print(f"Araba2 hizi : {araba2.hiz()}")
araba2.hizlan(20)
araba2.hizi = 180
print(f"Arabanin hizi :{araba2.hizi}")
araba.bilgi_goster()
