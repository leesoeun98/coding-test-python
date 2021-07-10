n, m = map(int, input().split())
matrix=[1]*n
res=[0]*n
check=[0]*(n+1)
for i in range(1, n):
    matrix[i] = matrix[i - 1] * (n - i) // i

def dfs(depth, sumnum):
    if depth==n and sumnum==m:
        print(*res)
        exit(0)
    for i in range(1, n+1):
        if check[i]==0:
            res[depth]=i
            check[i]=1
            dfs(depth+1, sumnum+matrix[depth]*res[depth])
            check[i]=0

dfs(0, 0)