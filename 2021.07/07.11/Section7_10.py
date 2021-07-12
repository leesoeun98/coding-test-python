board = [list(map(int, input().split())) for _ in range(7)]
visited=[[0]*7 for _ in range(7)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
cnt = 0


def dfs(i, j):
    global cnt
    if i == 6 and j == 6:
        cnt += 1
        return
    for d in range(4):
        nearx = i + xd[d]
        neary = j + yd[d]
        if 0 <= nearx < 7 and 0 <= neary < 7 and board[nearx][neary] == 0 and visited[nearx][neary]==0:
            visited[nearx][neary]=1
            dfs(nearx, neary)
            visited[nearx][neary]=0


visited[0][0]=1
dfs(0, 0)
print(cnt)
