n, m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
res=[0 for i in range(m)]
check=[0 for i in range(n)]
def DFS(depth, start):
    if depth==m:
        print(*res)
        return
    else:
        for i in range(start, n):
            res[depth]=num[i]
            DFS(depth+1, i+1)
DFS(0, 0)