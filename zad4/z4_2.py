def silnia(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * silnia(n-1)

plik = open('liczby.txt', 'r')
lista = plik.readlines()
plik.close()

liczby = [int(i.rstrip('\\n')) for i in lista]
poprawne = []
for i in liczby:
    suma = 0
    for x in str(i):
        suma += silnia(int(x))
    if suma == i:
        poprawne.append(i)

wynik_2 = poprawne
plik = open("wyniki4.txt", "w")
plik.writelines("4.2: {}\n".format(wynik_2))
plik.close()
