n, m = map(int, input().split())
sumnum=[0 for i in range(n+m+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sumnum[i+j]+=1
for i in range(len(sumnum)):
    if sumnum[i]==max(sumnum):
        print(i, end=" ")