T=[2,1,3,7,2,0,2,2,8,3,6,1]

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

QuickSort(T,len(T)-1)
print(T)
