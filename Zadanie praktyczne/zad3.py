plik = open('liczby.txt', 'r')
lista = plik.readlines()
plik.close()
numbers = [int(i.strip('\n')) for i in lista]


trojki = []

for i in range(0, len(numbers)):
    l_1 = int(numbers[i])
    for j in range(0, len(numbers)):
        if(i == j):
            continue

        l_2 = int(numbers[j])
        if(l_2 % l_1 == 0):
            for k in range (0, len(numbers)):
                if(i == k or j == k):
                    continue

                l_3 = int(numbers[k])
                if(l_3 % l_2 == 0):
                    trojki.append([l_1, l_2, l_3])





piatki = []

for i in range(0, len(numbers)):
    l_1 = int(numbers[i])
    for j in range(0, len(numbers)):
        if(i == j):
            continue

        l_2 = int(numbers[j])
        if(l_2 % l_1 == 0):
            for k in range (0, len(numbers)):
                if(i == k or j == k):
                    continue

                l_3 = int(numbers[k])
                if(l_3 % l_2 == 0):
                    for m in range(0, len(numbers)):
                        if(i == m or j == m or k == m):
                            continue

                        l_4 = int(numbers[m])
                        if(l_4 % l_3 == 0):
                            for n in range(0, len(numbers)):
                                if(i == n or j == n or k == m or m == n):
                                    continue

                                l_5 = int(numbers[n])
                                if(l_5 % l_4 == 0):
                                    piatki.append([l_1, l_2, l_3,l_4,l_5])





print(len(trojki))

for i in trojki:
    print(i)
print()
print(len(piatki))