# aciklama satiri
"""
Aciklama satiri
Aciklama satiri
"""

isim = "muhammet"
kullanici = """
Kullanici : Muhammet
TC : 8989779798797
"""
print(isim)
print(kullanici)

isim = 'muhammet'
kullanici = '''
Kullanici : Muhammet
TC : 878877987
'''
print(isim)
print(kullanici)

print(f"2:4 araligi = {isim[2:-1]}")
print(f"isim uzunlugu = {len(isim)}")
print(f"ISIM = {isim.upper()}")
print(f"isim = {isim.lower()}")

isim= "   muhammet    "
print(f"*{isim.strip()}*")


print(f"replace : {isim.replace("mm","nn")}")
text = "Python,Java,C++"
print(text.split(","))

liste = text.split(",")
print("+".join(liste))

print(text.find("Java"))

print(f"{text} ifadesi Py ile baslar :{text.startswith("Py")}")
print(f"{text} ifadesi \"++\" ile sonlanir : {text.endswith("++")}")

print(f"o harfi {text.count("o")} kez gecer.")
isim = "Ali"
yas = 25
print("Merhaba, ben {} ve {} yaşındayım.".format(isim, yas))

print('merhaba\nBen Muhammet\t Ogretmenim \'\'')
print("Merhaba " * 3 )
print("py" in "python")