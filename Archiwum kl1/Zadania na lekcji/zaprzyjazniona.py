def zaprzyjazniona (a, b):
    sumaA=int(0)
    sumaB=int(0)
    dzielnik=int(1)

    while(dzielnik<a):
        if (a%dzielnik==0):
            sumaA+=dzielnik
            dzielnik+=1

        else:
            dzielnik+=1

    dzielnik=1

    while(dzielnik<b):
        if(b%dzielnik==0):
            sumaB+=dzielnik
            dzielnik+=1
                
        else:
            dzielnik+=1

    if (sumaA==b and sumaB==a) :
        return "Tak"

    else:
        return "Nie"

x=int(input ("podaj x "))
y=int (input ("podaj y "))

print(zaprzyjazniona(x, y))
