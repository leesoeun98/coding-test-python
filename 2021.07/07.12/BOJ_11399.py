n = int(input())
time=list(map(int, input().split()))
time.sort()
res=0
for i in range(n):
    wait=0
    for j in range(i):
        wait+=time[j]
    res+=(wait+time[i])

print(res)