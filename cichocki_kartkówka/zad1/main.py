n = int(input("Podaj n: "))
c = n//2
t = []

for i in range(n):
    x = []
    for j in range(c):
        x.append("none")
    t.append(x)

for i in range(n):
    for j in range(c):
        print(t[i][j], end="\t")
    print()
