from collections import deque

board = [list(map(int, input().split())) for i in range(7)]
check = [[0] * (7) for i in range(7)]
count = [[0] * (7) for i in range(7)]
end = (6, 6)
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
queue = deque()
# 초기화
queue.append((0, 0))
check[0][0] = 1
count[0][0] = 0
while queue:
    x, y = queue.popleft()
    # 종료조건
    if x == 6 and y == 6:
        break
    for direction in range(4):
        nearx = x + xd[direction]
        neary = y + yd[direction]
        if 0 <= nearx <= 6 and 0 <= neary <= 6:
            if board[nearx][neary] == 0 and check[nearx][neary] == 0:
                check[nearx][neary] = 1
                count[nearx][neary] = count[x][y] + 1
                queue.append((nearx, neary))
if count[6][6]==0:
    print(-1)
else:
    print(count[6][6])
