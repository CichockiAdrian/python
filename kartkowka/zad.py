import random
x=int(input("Podaj ilość haseł do wygenerowania: "))
i=10

m=True
l=input("Czy mam używać tylko małych liter(y/n): ")
if l=="n":
    m=False
    
    
n=False
p=input("Czy mam używać liczb(y/n): ")
if p=="y":
    n=True
    
z=False
c=input("Czy mam używać znaków specjalnych(y/n): ")
if c=="y":
    z=True

al_d=["A", "B",	"C", "D", "E", "F",	"G", "H", "I", "J",	"K", "L", "M", "N",	"O", "P", "Q", "R",	"S", "T", "U", "V",	"W", "X", "Y", "Z"]
al_m=["a", "b",	"c", "d", "e", "f",	"g", "h", "i", "j",	"k", "l", "m", "n",	"o", "p", "q", "r",	"s", "t", "u", "v",	"w", "x", "y", "z"]
num=range(10)
znk=["!","@","#","$","%","^","&","*","(",")","_","+","-","="]

hasla=[]

for j in range(x):
    has=""
    b1=m
    b2=n
    b3=z
    for k in range(i):
        if(len(has)<i):
            q=random.choice(al_m)
            has=has+q
            if(m==False):
                q=random.choice(al_d)
                has=has+q
                m=True
            elif(z==True):
                q=random.choice(znk)
                has=has+q
                z=False
            elif(n==True):
                q=str(random.choice(num))
                has=has+q
                n=False
    m=b1
    n=b2
    z=b3
    hasla.append(has)
    
print(hasla)
plik = open("wyniki.txt", "w")
plik.writelines("{}\n".format(hasla))
plik.close()