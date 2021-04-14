n, m = map(int, input().split())
adj = [[0 for i in range(n)] for i in range(n)]
check=[0 for i in range(n)]
for _ in range(m):
    start, end = map(int, input().split())
    adj[start-1][end-1] = 1
path=[]
count = 0
check[0]=1
path.append(1)

def DFS(depth):
    global count, path
    if depth==n-1:
        count+=1
        print(*path)
        return
    else:
        for i in range(n):
            if adj[depth][i]==1 and check[i]==0:
                check[i]=1
                path.append(i)
                DFS(i)
                check[i]=0
                path.pop()
DFS(0)
print(count)