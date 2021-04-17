n, m = map(int, input().split())
res=[0 for i in range(m)]
count=0
def DFS(depth):
    global count
    if depth==m:
        print(*res)
        count+=1
        return
    else:
        for i in range(n):
            res[depth]=i+1
            DFS(depth+1)
DFS(0)
print(count)