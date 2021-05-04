n=int(input())
def count(num):
    cnt=0
    nm=list(str(num))
    for n in nm:
        n=int(n)
        if n==3 or n==6 or n==9:
            cnt+=1
    return cnt


for i in range(1, n+1):
    cnt=count(i)
    if cnt==0:
        print(i, end=" ")
    else:
        for c in range(cnt):
            print('-', end="")
        print(' ', end="")