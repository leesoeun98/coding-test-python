for t in range(1, int(input())+1):
    res=0
    n=int(input())
    for i in range(1, n+1):
        if i%2==0:
            res-=i
        else:
            res+=i
    print("#"+str(t)+" "+str(res))