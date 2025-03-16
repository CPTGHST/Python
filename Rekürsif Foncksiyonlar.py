# n den 1 kadar olan sayilar ekrana yazdira program
"""from pprint import pprint

def pprint(n):
    if n <= 1:
        return n
    print(n , end=",")
    return pprint(n-1)
pprint(5)"""
"""from pprint import pprint


def pprint(n):
    if n > 1:
       pprint(n-1)
    print(n, end =' ')
pprint(5)"""

#faktoriyel ornek

"""def faktoriyel(n):
    if n <= 1:
       return n
    else:
       return n*faktoriyel(n-1)
print(faktoriyel(5))"""

#fibonnaci ornek

#Verilen listenin sayılarını toplamını rekürsif şekilde yazınız

def dizi_toplam(x):
    print(x)
    if len(x) == 0:
        return 0
    return x[0] + dizi_toplam(x[1:])

print(dizi_toplam([3,4,5]))






