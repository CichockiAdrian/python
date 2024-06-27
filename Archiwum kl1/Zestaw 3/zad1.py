from collections import Counter 
def Moda(T):
    c=0
    data = Counter(T) 
    moda = dict(data) 
    P = [k for k, v in moda.items() if v == max(list(data.values()))] 
    for i in range(len(T)-1):
        if(T[i]!=T[i+1]):
           c=c+1
    if (len(P) == n): 
        moda = "Nie ma Mody" 
    elif(len(P*2)==n): 
        moda = "Nie ma mody"
    elif(len(P)==n/len(P)): 
        moda = "Nie ma mody"
    elif(len(P)==n/c): 
        moda = "Nie ma mody"
    else: 
        moda = "Moda jest lub są liczby: " + ', '.join(map(str, P)) 
         
    return(moda) 
 
T = [1,1,1,1,2,2,2,2,3,3,3,3] 
n = len(T) 
print(Moda(T)) 
 
