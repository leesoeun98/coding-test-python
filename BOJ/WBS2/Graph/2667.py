from collections import deque
xd=[-1,1,0,0]
yd=[0,0,1,-1]
"""def DFS(i, j):
    global cnt
    cnt+=1
    visited_dfs[i][j]=count
    for direction in range(4):
        x=i+xd[direction]
        y=j+yd[direction]
        if 0<=x<n and 0<=y<n and visited_dfs[x][y]==0 and maps[x][y]==1:
            visited_dfs[x][y]=count
            DFS(x, y)"""
def BFS(i, j):
    queue.append((i, j))
    count=1
    visited_bfs[i][j]=1
    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nearx=x+xd[direction]
            neary=y+yd[direction]
            if 0<=nearx<n and 0<=neary<n and visited_bfs[nearx][neary]==0 and maps[nearx][neary]==1:
                queue.append((nearx, neary))
                visited_bfs[nearx][neary]=1
                count+=1
    answer.append(count)

n = int(input())
maps=[list(map(int, input())) for _ in range(n)]
visited_dfs=[[0]*n for _ in range(n)]
visited_bfs=[[0]*n for _ in range(n)]
#count=1
answer=[]
queue=deque()
for i in range(n):
    for j in range(n):
        if visited_bfs[i][j]==0 and maps[i][j]==1:
            BFS(i, j)

"""for i in range(n):
    for j in range(n):
        if visited_dfs[i][j]==0 and maps[i][j]==1:
            cnt=0
            DFS(i, j)
            count+=1
            answer.append(cnt)"""
answer.sort()
print(len(answer))
for a in answer:
    print(a)
