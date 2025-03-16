meyveler = ["elma","armut", "portakal"]

for m in meyveler:
    print(m)

#[0,1,2,3,4]
for i in range(-3,10,2):
    print(i)

i = 0
while i < 5:
    print(i)
    i = i + 1
    #i += 1
print("#" * 10 )
print("break ve continue")
print("#" * 10 )

for i in range(10):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)


for i in range(6):
    if i == 3:
        break
    print(i)

def selam_ver(isim):
    print("Merhaba",isim)

selam_ver("Muhammet")
selam_ver(["Ali","veli"])

def foo():
    print("Hello")

foo()

def toplama(a,b):
    print(a+b)

toplama(10,10)
toplama("ali","veli")

def selam_ver(isim="Muhammet"):
    print("Merhaba",isim)

selam_ver()
selam_ver("Ali")