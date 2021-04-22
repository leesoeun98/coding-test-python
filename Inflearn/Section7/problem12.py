n = int(input())
board = [list(map(int, input())) for i in range(n)]
house=[[0]*n for i in range(n)]
res = []
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
index=1
def DFS(x, y):
    global count
    count+=1
    board[x][y]=0
    house[x][y]=index
    for i in range(4):
        nearx = x + xd[i]
        neary = y + yd[i]
        if 0 <= nearx < n and 0 <= neary < n and board[nearx][neary] == 1:
            DFS(nearx, neary)

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            count=0
            DFS(i, j)
            res.append(count)
            index+=1
print(len(res))
res.sort()
for r in res:
    print(r)
