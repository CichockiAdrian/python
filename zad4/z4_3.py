plik = open('liczby.txt', 'r')
lista = plik.readlines()
plik.close()

liczby = [int(i.rstrip('\\n')) for i in lista]
poprawne = []
for i in range(len(liczby)):
    ciag = [liczby[i]]
    for j in range(i+1, len(liczby)):
        ciag.append(liczby[j])
        dzielniki = set()
        for k in ciag:
            dzielniki |= set([i for i in range(2, k+1) if k % i == 0])
        if max(dzielniki) > 1:
            if len(ciag) > len(poprawne):
                poprawne = ciag.copy()
        else:
            break

if poprawne:
    wynik_4_3 = (poprawne[0], len(poprawne), max(dzielniki))
else:
    wynik_4_3 = None

plik = open("wyniki4.txt", "w")
plik.writelines("4.3: {}\n".format(wynik_4_3))
plik.close()