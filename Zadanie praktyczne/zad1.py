plik = open('liczby.txt', 'r')
lista = plik.readlines()
plik.close()
c=0
liczby = [i.strip('\n') for i in lista]
for i in liczby:
    i = str(i)
    if(i[0]==i[-1]):
        c+=1
        if(c==1):
            print (i)
        
print (c)