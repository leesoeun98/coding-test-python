#1차 시도 실패 
n, m = map(int, input().split())
weight=list(map(int, input().split()))
check=[0 for i in range(n)]
weight.sort()
boats=0
for i in range(n-1):
    if check[i]==0:
        for j in range(i, n):
            if check[j]==0 and weight[i]+weight[j]<=m:
                check[i]=1
                check[j]=1
                boats+=1
print(boats)
print(check)

