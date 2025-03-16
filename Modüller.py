import os
from sys import excepthook

"""for file in os.listdir("C:\\"):
    print(file)"""

"""print(os.getcwd())
#print(os.chdir("C:\\"))
for file in os.listdir("C:\\"):
    print(file)

file = "yeni_klasör"""
"""try:
    os.mkdir(file)
except FileExistsError:
    print("var olan dosya")
    os.mkdir(file)
    os.rmdir(file)"""

#os.rmdir(file)
"""print("Dosya var"if os.path.exists(file) else "Dosya yok")

basicfile = "silinecek.txt"
if  os.path.exists(basicfile):
    os.remove(basicfile)
else:
    print("Dosya yok")

print(os.getenv("COMPUTERNAME"))
os.environ["LISANS_KEY"] = "233565326556032"
print(os.getenv("LISANS_KEY"))"""

print(os.name)
#os.rename("gecici_dosya","silinecek_dosya ")
print(os.getcwd())

fd = open("yeni_dosya.txt","w")
fd.write("merhaba")
fd.close()

fd = open("yeni_dosya.txt","w")
fd.write("merhaba1")
fd.close()

fd = open("yeni_dosya.txt","r")
print(fd.read())
fd.close()

with open("yeni_dosya.txt","r") as fd:
    print(fd.readlines())

