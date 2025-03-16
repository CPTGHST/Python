x = ()
print(x,type(x))
x= (1,2,4,3,4)
print(x)
x= (1,2,3,4,4,"deneme")
print(x)

print(x[-1])

print(x[0:2])

print(x.count(4))

print(x.index(4))

#del x
liste = list(x)
print(liste)

x = [1,2,3]
print(x, type(x))

x = tuple(liste)
print(x,type(x))