n=int(input())
num=list(map(int, input().split()))
length=[1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[i]>num[j] and length[j]+1>length[i]:
            length[i]=length[j]+1
print(max(length))
