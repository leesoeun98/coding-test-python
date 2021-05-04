for t in range(1, int(input())+1):
    res=0
    num=list(map(int, input().split()))
    for n in num:
        if n==min(num):
            continue
        elif n==max(num):
            continue
        else:
            res+=n
    avg=round(res/8)
    print("#"+str(t)+" "+str(avg))