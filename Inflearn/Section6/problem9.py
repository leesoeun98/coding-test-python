n, f = map(int, input().split())
res=[[0 for i in range(n)] for i in range(n)]
def DFS(depth, final):
    if depth==n:
        print(res)
        return
    else:
        for i in range(n-depth):
            res[i][i]=final
            DFS(depth+1, res[i]+res[i+1])

DFS(0, 1)