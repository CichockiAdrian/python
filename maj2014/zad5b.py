nazwa_pliku = '/Users/adrianc/PycharmProjects/maj2014/NAPIS.txt'

plik = open(nazwa_pliku)

file = plik.readlines()
ros = []

for line in file:
    line = line.strip()
    b = True
    for i in range(1, len(line)):
        if ord(line[i]) <= ord(line[i - 1]):
            b = False
            break

    if b:
        ros.append(line)

c=0
for word in ros:
    print(word)
    c=c+1
print(c)