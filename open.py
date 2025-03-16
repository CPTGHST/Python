#open (dosya_ismi, modu)
#w,a,r,b(modlar)

with open("yeni_dosya.txt", "r") as fd:
    print(fd.readline())
    print(fd.readline())
    print(fd.readline())
    fd.seek(0)
    print(fd.readline())

with open("yeni_dosya.txt","r+") as fd:
    lines = fd.readlines()
    print(f"Last line : {lines[-1]}")
    lines[-1] = "Last line changed"
    fd.seek(0)
    fd.writelines(lines)

with open("human.jpg","r+b") as fd:
    data = fd.read()

with open("human_copy.jpg","w+b") as fd:
    fd.write(data)

import os
if os.path.exists("yeni_dosya.txt"):
    print("File available")

