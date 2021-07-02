graph=[]
n=int(input())
x=[-1, 1, 0, 0]
y=[0, 0, -1, 1]

for _ in range(n):
    temp=list(map(int, input()))
    graph.append(temp)

def dfs(i, j):
    global cnt
    for direction in range(4):
        nearx=x[direction]+i
        neary=y[direction]+j
        if 0<=nearx<n and 0<=neary<n and graph[nearx][neary]==1:
            cnt+=1
            graph[nearx][neary]=0
            dfs(nearx, neary)

res=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt=1
            graph[i][j]=0
            dfs(i, j)
            res.append(cnt)
res.sort()
print(len(res))
for r in res:
    print(r)

