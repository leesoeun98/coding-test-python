import sys
sys.setrecursionlimit(10**6)
n = int(input())
board=[list(map(int, input().split())) for _ in range(n)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]
res=[]
def dfs(i, j, rain):
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]>rain and visited[nearx][neary]==0:
            visited[nearx][neary]=1
            dfs(nearx, neary, rain)

for rain in range(101):
    cnt=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]>rain and visited[i][j]==0:
                visited[i][j]=1
                dfs(i, j, rain)
                cnt+=1
    res.append(cnt)
print(max(res))