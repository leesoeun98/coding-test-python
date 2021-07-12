board=[list(map(int, input().split())) for _ in range(10)]
visited=[[0]*10 for _ in range(10)]
def dfs(i, j):
    if i==0:
        print(j)
        exit(0)
    else:
        if 0<=j-1<10 and board[i][j-1]==1 and visited[i][j-1]==0:
            visited[i][j-1]=1
            dfs(i, j-1)
        elif 0<=j+1<10 and board[i][j+1]==1 and visited[i][j+1]==0:
            visited[i][j+1]=1
            dfs(i, j+1)
        else:
            visited[i-1][j]=1
            dfs(i-1, j)

for i in range(10):
    if board[9][i]==2:
        dfs(9, i)
