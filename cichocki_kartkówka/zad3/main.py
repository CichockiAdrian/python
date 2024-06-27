string = "kamil to czlowiek"

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
spolgloski = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z']
str_samo=""
str_spol=""
c_samo=0
c_spol=0
for i in range(len(string)):
    for k in range(len(samogloski)):
        if(string[i]==samogloski[k]):
            c_samo+=1
            str_samo+=string[i]
for i in range(len(string)):
    for k in range(len(spolgloski)):
        if(string[i]==spolgloski[k]):
            c_spol+=1
            str_samo+=string[i]

print(string+" -> liczba spolglosek:"+str(c_spol)+", liczba samoglosek: "+str(c_samo)+", ciąg:"+str_samo+str_spol)
