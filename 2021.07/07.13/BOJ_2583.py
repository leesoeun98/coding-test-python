import sys
sys.setrecursionlimit(10**6)
m, n, k = map(int, sys.stdin.readline().split())
paper=[[0]*n for _ in range(m)]
visited=[[0]*n for _ in range(m)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]
for _ in range(k):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    row=ex-sx
    col=ey-sy
    for i in range(col):
        for j in range(row):
            paper[sy+i][sx+j]=1

def dfs(i, j):
    global cnt
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<m and 0<=neary<n and paper[nearx][neary]==0 and visited[nearx][neary]==0:
            visited[nearx][neary]=1
            cnt+=1
            dfs(nearx, neary)
res=[]
for i in range(m):
    for j in range(n):
        if paper[i][j]==0 and visited[i][j]==0:
            visited[i][j]=1
            cnt=1
            dfs(i, j)
            res.append(cnt)
res.sort()
print(len(res))
print(*res)
