n, m = map(int, input().split())
res=[0 for i in range(m)]
def DFS(depth):
    if depth==m:
        print(*res)
        return
    else:
        for i in range(n):
            res[depth]=i+1
            DFS(depth+1)
DFS(0)