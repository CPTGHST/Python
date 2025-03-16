bos_kume = set()
print(f"Bos kume : {bos_kume} veri tipi : {type(bos_kume)}")
kume1 = {1,2,3,3,4}

print(f"Kume1 : {kume1}")

kume1.add(100)
print(f"100 eklendi : {kume1}")

kume1.discard(10)
print(f"Discard sonrasi:{kume1}")

#kume1.remove(10)
print(f"100 silindi : {kume1}")

#kume1.discard(10)

# Birlesim islemi
kume1 = {1,2,3,3,4}
kume2 = {2,3,5,6}

print(f"Birlesim islemi sonrasi : {kume1 | kume2}")

print(f"Kesisim islemi sonrasi : {kume1 & kume2}")

print(f"Kume farki : {kume1 - kume2 }")

#kume1 - kume2 | kume2 - kume1
print(f"Simetrik fark :{kume1 ^ kume2}")

donmus_kume = frozenset([1,2,3,4])
print(donmus_kume)
