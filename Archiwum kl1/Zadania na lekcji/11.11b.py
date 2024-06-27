def prz(a):
    c=int(0)
    p=int(a)
    
    while(p>0):
        p=p//10
        c=c+1
    
    c=c-1
    while(a>0):
        print(a//(10**c))
        a=a%(10**c)
        c=c-1
    
x=int(input ("podaj x "))

print(prz(x))
