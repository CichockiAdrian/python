nazwa_pliku = '/Users/adrianc/PycharmProjects/maj2014/NAPIS.txt'

plik = open(nazwa_pliku)

file = plik.readlines()
same = []

for line in file:
    c=0
    line = line.strip()
    for i in file:
        i=i.strip()
        if line == i:
            c=c+1
    if c>1 and line not in same:
        same.append(line)
    c=0
for i in same:
    print(i)