import sys
sys.setrecursionlimit(10**6)
n = int(input())
board=[list(input()) for _ in range(n)]
board_week=board.copy()
visited=[[0]*n for _ in range(n)]
visited_week=[[0]*n for _ in range(n)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]

def dfs(i, j, graph, visited_graph):
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and graph[i][j]==graph[nearx][neary] and visited_graph[nearx][neary]==0:
            visited_graph[nearx][neary]=1
            dfs(nearx, neary, graph, visited_graph)
cnt=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            visited[i][j]=1
            dfs(i, j, board, visited)
            cnt+=1

for i in range(n):
    for j in range(n):
        if board_week[i][j]=='G':
            board_week[i][j]='R'

cnt_week=0
for i in range(n):
    for j in range(n):
        if visited_week[i][j]==0:
            visited_week[i][j]=1
            dfs(i, j, board_week, visited_week)
            cnt_week+=1
print(cnt, cnt_week)

