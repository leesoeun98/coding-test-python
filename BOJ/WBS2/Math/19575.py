import sys
n, x = map(int,sys.stdin.readline().split())
res=0
mod=10**9+7
for i in range(n+1):
    a, b = map(int,sys.stdin.readline().split())
    if i==0:
        res=a
    else:
        res=(res*x+a)%mod
print(res)