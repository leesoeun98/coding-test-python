n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
check = [[0] * (n) for i in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
count = 0
maxx = -987654321
minn = 987654321
# 시작, 끝 위치 찾는 거 주의
endx = endy = startx = starty = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > maxx:
            maxx = board[i][j]
            endx = i
            endy = j
        if board[i][j] < minn:
            minn = board[i][j]
            startx = i
            starty = j


def DFS(x, y):
    global count
    if x == endx and y == endy:
        count += 1
        return
    else:
        for i in range(4):
            nearx = x + xd[i]
            neary = y + yd[i]
            if 0 <= nearx < n and 0 <= neary < n and check[nearx][neary] == 0 and board[x][y] < board[nearx][neary]:
                check[nearx][neary] = 1
                DFS(nearx, neary)
                check[nearx][neary] = 0


check[startx][starty] = 1
DFS(startx, starty)
print(count)
