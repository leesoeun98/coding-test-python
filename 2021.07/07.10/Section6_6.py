n, m = map(int, input().split())
res=[0]*m
cnt=0
def dfs(depth):
    global cnt
    if depth==m:
        print(*res)
        cnt+=1
        return
    else:
        for i in range(1, n+1):
            res[depth]=i
            dfs(depth+1)

dfs(0)
print(cnt)