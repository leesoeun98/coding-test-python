n = int(input())
board=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]
sx, sy, ex, ey = 0,0,0,0
minh=987654321
maxh=0
cnt=0
for i in range(n):
    for j in range(n):
        if board[i][j]<minh:
            minh=board[i][j]
            sx=i
            sy=j
        if board[i][j]>maxh:
            maxh=board[i][j]
            ex=i
            ey=j
def dfs(i, j):
    global cnt
    if i==ex and j==ey:
        cnt+=1
        return
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]>board[i][j] and visited[nearx][neary]==0:
            visited[nearx][neary]=1
            dfs(nearx, neary)
            visited[nearx][neary]=0
visited[sx][sy]=1
dfs(sx, sy)
print(cnt)
