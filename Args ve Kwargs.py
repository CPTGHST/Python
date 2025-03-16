def topla(*args):
    print(type(args))
    print(args)


topla(1,2,)
topla(1,2,3)
topla(1,2,3,4)

def kisi_bilgisi(kwargs):
    print(kwargs,type(kwargs))

kisi_bilgisi(isim="Muhammet", soyisim="ozturk")
kisi_bilgisi(isim="Muhammet", soyisim="ozturk",yas=32)

