def transposition(t):
    for row in t :

        print(row)

    t = [[t[j][i] for j in range(len(t))] for i in range(len(t[0]))]

    print("\n")

    for row in t:

        print(row)

