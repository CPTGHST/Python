import random

print(random.random())
print(random.randint(1,10))

print(random.choice(["Matrix","Matrix 2","Matrix 3"]))
print(random.choices(["Matrix","Matrix 2","Matrix 3"],k=2))

liste =["Matrix","Matrix 2","Matrix 3"]
random.shuffle(liste)
print(liste)

