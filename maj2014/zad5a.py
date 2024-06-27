nazwa_pliku = '/Users/adrianc/PycharmProjects/maj2014/NAPIS.txt'

def is_prime(x):
    if x < 2:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True



t=[]
q=[]
plik = open(nazwa_pliku)

file = plik.readlines()
for i in file:
    i=i[:-1]
    t.append(i)

for i in t:
    c = 0
    for j in i:
        c=c+ord(j)
    if(is_prime(c)):
        q.append(i)
        
print("Ilość liczb pierwszych:")
print(len(q))

  


