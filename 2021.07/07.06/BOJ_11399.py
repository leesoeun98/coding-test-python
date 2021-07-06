n = int(input())
time=list(map(int, input().split()))
time.sort()
res=0
for i in range(n, 0, -1):
    res+=time[n-i]*i
print(res)