n=4
c=0
t=0
res=n*n-1
for i in range(1,n+1):
    space=0
    while space<=2*i:
        print(" ",end=" ")
        space=space+1
    t=res
    for j in range(1,n-(i-1)+1):
        c=c+1
        print(c,end="")
    for k in range(1,n-(i-1)+1):
        print(t,end="")
        t=t+1
    res=res-(i+1)
    print()
