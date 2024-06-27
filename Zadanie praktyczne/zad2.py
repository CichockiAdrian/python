import math

def count_pierwsze(n):
    c = 0
    while n % 2 == 0:
        c += 1
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            c += 1
            n //= i
    if(n > 2):
        c += 1
    return c

def count_unikalne(n):
    cz = set()
    while n % 2 == 0:
        cz.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            cz.add(i)
            n //= i
    if(n > 2):
        cz.add(n)
    return cz

plik = open('liczby.txt', 'r')
lista = plik.readlines()
plik.close()
numbers = [int(i.strip('\n')) for i in lista]
max_liczba = 0
max_liczba_count = 0
max_unik = 0
max_unik_count = 0

for i in numbers:
    czynniki_pierwsze = count_pierwsze(i)
    unik_pierwsze = len(count_unikalne(i))
    if(czynniki_pierwsze > max_liczba):
        max_liczba = czynniki_pierwsze
        max_liczba_count = i
    if(unik_pierwsze > max_unik):
        max_unik = unik_pierwsze
        max_unik_count = i



print(max_liczba)
print()
print (max_liczba_count)
print()
print(max_unik)
print()
print(max_unik_count)