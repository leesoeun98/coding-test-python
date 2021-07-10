import sys
sys.setrecursionlimit(10**6)
n = int(input())
board=[list(input()) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
visited_week=[[0]*n for _ in range(n)]
board_week=board.copy()

xd=[-1,1,0,0]
yd=[0,0,-1,1]

def dfs_week(i, j):
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board_week[nearx][neary]==board_week[i][j] and visited_week[nearx][neary]==0:
            visited_week[nearx][neary]=1
            dfs_week(nearx, neary)
def dfs(i, j):
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]==board[i][j] and visited[nearx][neary]==0:
            visited[nearx][neary]=1
            dfs(nearx, neary)

cnt_week=0
cnt=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i, j)
            cnt+=1
        if board_week[i][j]=='R':
            board_week[i][j]='G'
for i in range(n):
    for j in range(n):
        if visited_week[i][j]==0:
            dfs_week(i, j)
            cnt_week+=1
print(cnt, cnt_week)
