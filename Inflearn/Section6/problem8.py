n, m = map(int, input().split())
selected=[0 for i in range(m)]
isvisited=[False for i in range(n)]
count=0
def DFS(depth):
    global count
    if depth==m:
        count+=1
        print(*selected)
        return
    else:
        for i in range(n):
            if not isvisited[i]:
                isvisited[i]=True
                selected[depth]=i+1
                DFS(depth+1)
                isvisited[i]=False
DFS(0)
print(count)

