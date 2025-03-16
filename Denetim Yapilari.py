#== , > , < , <= , != , >=
# İki sayı tanımlıyoruz
a = 10
b = 5

# Eşitlik operatörü (==)
print(f"{a} == {b}: {a == b}")  # False

# Eşit değil operatörü (!=)
print(f"{a} != {b}: {a != b}")  # True

# Büyükten küçüğe operatörü (>)
print(f"{a} > {b}: {a > b}")    # True

# Küçükten büyüğe operatörü (<)
print(f"{a} < {b}: {a < b}")    # False

# Büyük eşit operatörü (>=)
print(f"{a} >= {b}: {a >= b}")  # True

# Küçük eşit operatörü (<=)
print(f"{a} <= {b}: {a <= b}")  # False

if a != b:
    print("Esit degildir.")

elif a == 10 : #  else if
    print("10 esittir.")

else :
    print("hic bir sart sagflanmadi.")

print("Program bitti .")

x = 100
#and ve or
if x > 10  and x < 20:
    """
    Aciklama satiri
    """
    print("10 ile 20 arasindadir")
elif x > 10  or x < 20:
    print("100 e esittir.")
else:
    print("Sartlar saglanmadi.")
print("Bitti.")

