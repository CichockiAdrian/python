
alfabet=['t','u','v','k','l','m','n','w','f','x','y','z','g','h','i','j','o','p','a','b','c','d','e','r','s','q']
text="gruz"
sort=""
ts=[]
for i in range(len(text)):
    for k in range(len(alfabet)):
        if(text[i]==alfabet[k]):
            ts.append((k))


#quicksort z archiwum
def Divide(T,p,r):
    q=p+(r-p)//2
    x=T[q]
    k=T[q]
    T[q]=T[r]
    T[r]=k
    j=p
    for i in range(p,r):
        if T[i] <x:
            k=T[i]
            T[i] = T[j]
            T[j]=k
            j=j+1
    k=T[j]
    T[j]=T[r]
    T[r]=k
    return j

def QuickSortPart(T,p,r):
    if p<r:
        q=Divide(T,p,r)
        QuickSortPart(T,p,q-1)
        QuickSortPart(T,q+1,r)

def QuickSort(T,n):
    QuickSortPart(T,0,n)

QuickSort(ts,len(ts)-1)

for i in range(len(alfabet)):
    for j in range(len(ts)):
        if(i==ts[j]):
            sort+=alfabet[i]

print(text+"->"+sort)