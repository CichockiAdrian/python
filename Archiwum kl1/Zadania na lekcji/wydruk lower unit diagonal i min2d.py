t=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
def wydruk(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            print(t[i][j], end=" ")
        print()


def unit(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if(i==j):
                t[i][j]=1
            else:
                t[i][j]=0


def diagonal(t):
    s=0
    for i in range(len(t)):
        for j in range(len(t[i])):
            if(i==j):
                s=s+t[i][j]
    return(s)

def lower(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if(i>j):
                t[i][j]=9


def min2d(t):
    m=int(t[0][0])
    for i in range(len(t)):
        for j in range(len(t[i])):
            if(m>t[i][j]):
                m=t[i][j]
    return(m)

wydruk(t)
print("16.3")
unit(t)
wydruk(t)
print("16.4")
diagonal(t)
print(diagonal(t))
print("16.5")
lower(t)
wydruk(t)
print("16.6")
print(min2d(t))
