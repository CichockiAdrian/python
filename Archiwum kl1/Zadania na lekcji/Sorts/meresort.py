import math
T = [2,1,1,5,4,2,0,0,2,4,6]
n=len(T)
def MergeSort (T,n):
    T.append(None)
    T[-1]=T[0]
    MergeSortPart(T,1,n)
    T.pop(0)

def MergeSortPart(T,p,r):
    if p<r:
        q=(p+r)//2
        MergeSortPart(T,p,q)
        MergeSortPart(T,q+1,r)
        Merge(T,p,q,r)

def Merge(T,p,q,r):
    a = q-p+1
    b=r-q
    A = []
    for k in range(1,a+1,1):
        A.append(T[p+k-1])
    A.append(math.inf)
    B=[]
    for k in range(1,b+1,1):
        B.append(T[q+k])
    B.append(math.inf)
    i=0
    j=0
    for k in range (p,r+1,1):
        if A[i]<B[j]:
            T[k]=A[i]
            i=i+1
        else:
            T[k]=B[j]
            j=j+1

MergeSort(T,n)
print(T)

