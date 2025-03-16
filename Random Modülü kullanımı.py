import random
from idlelib.colorizer import prog_group_name_to_tag
print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))
print(random.choice([1,2,3,4,"test"]))
print(random.choices([1,2,3,4,5,6],k = 3))
liste = [1,2,3,4,5]
random.shuffle(liste)
print(liste)
print(random.sample([1,2,3,4,5],k = 3))

print(random.randrange(0,100,2))