def doskonala(a):
    dzielnik=int(1)
    suma=int(0)
    
    while (dzielnik<a):
        if (a%dzielnik==0):
            suma+=dzielnik
            dzielnik+=1

        else:
            dzielnik+=1

    if (suma==a) :
        return "Tak"
    else:
        return "Nie"

x=int(input ("podaj x "))
print(doskonala(x))
