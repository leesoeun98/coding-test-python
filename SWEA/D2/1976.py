for t in range(1, int(input()) + 1):
    t1, m1, t2, m2 = map(int, input().split())
    time=(t1+t2+(m1+m2)//60)%12
    if time==0:
        time=12
    minute=(m1+m2)%60
    print("#"+str(t)+" "+str(time)+" "+str(minute))

