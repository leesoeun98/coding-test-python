n = int(input())
#입력주의
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
        #0이면 돌 이유가 없음
        if board[i][j]==1:
            count=0
            DFS(i, j)
            #DFS끝나면 단지가 끝난것. BFS에서도 QUEUE가 끝나면 단지가 끝난 것
            res.append(count)
            index+=1
print(len(res))
res.sort()
for r in res:
    print(r)
