n, m = map(int, input().split())
sum=[0 for _ in range(41)]
for i in range (1, n+1):
    for j in range (1, m+1):
        sum[i+j]+=1
for i in range(len(sum)):
    if sum[i]==max(sum):
        print(i, end=" ")