potegi_3 = []
for i in range(12):
    potegi_3.append(3 ** i)

licznik = 0
plik = open('liczby.txt', 'r')
lista = plik.readlines()
plik.close()

liczby = [int(i.rstrip('\\n')) for i in lista]
for i in liczby:
    for dzielnik in potegi_3:
        if i == dzielnik:
            licznik += 1

wynik_1 = licznik
plik = open("wyniki4.txt", "w")
plik.writelines("4.1: {}\n".format(wynik_1))
plik.close()
