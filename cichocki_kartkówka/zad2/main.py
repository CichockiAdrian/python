n = int(input("Podaj n: "))
t = []

for i in range(n):
    x = []
    for j in range(n):
        x.append(j)
    t.append(x)

for i in range(n):
    for j in range(n):
        print(t[i][j], end="\t")
    print()
print()
for j in range(n):
    for i in range(n):
        print(t[i][j], end="\t")
    print()
