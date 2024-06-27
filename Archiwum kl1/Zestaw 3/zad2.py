def Cezar(T):
    n=len(T)
    Z=[None] * n
    A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
    d=len(A)
    for i in range(n):
        x=T[i]
        for j in range(d):
            if(x==A[j]):
                c=j+3
                Z[i]=A[c]
                break
    return(Z)

T=['c','e','z','a','r']
print(Cezar(T))
