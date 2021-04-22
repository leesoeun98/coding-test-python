from collections import deque

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
check = [[0] * (n) for i in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
mid = n // 2
queue = deque()
count = 0

# 초기화
queue.append((mid, mid))
check[mid][mid] = 1
count += board[mid][mid]
index = 0
while queue:
    # 종료조건 만들어주기
    if index == mid:
        break
    for i in range(len(queue)):
        x, y = queue.popleft()
        for direction in range(4):
            nearx = x + xd[direction]
            neary = y + yd[direction]
            if 0 <= nearx <= n - 1 and 0 <= neary <= n - 1 and check[nearx][neary] == 0:
                check[nearx][neary] = 1
                count += board[nearx][neary]
                queue.append((nearx, neary))
    index += 1
print(count)
