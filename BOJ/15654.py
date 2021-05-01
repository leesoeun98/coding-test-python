n, m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
res=[0 for i in range(m)]
check=[0 for i in range(n)]
def DFS(depth):
    if depth==m:
        print(*res)
        return
    else:
        for i in range(n):
            if check[i]==0:
                res[depth]=num[i]
                check[i]=1
                DFS(depth+1)
                check[i]=0

DFS(0)
