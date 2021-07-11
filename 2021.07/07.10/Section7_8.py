from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
queue = deque()
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
mid = n // 2
idx = 0
total = 0

queue.append((mid, mid))
visited[mid][mid] == 1
#왜 가운데거는????

while queue:
    if idx == mid:
        break
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for d in range(4):
            nearx = x + xd[d]
            neary = y + yd[d]
            if 0 <= nearx < n and 0 <= neary < n and visited[nearx][neary] == 0:
                visited[nearx][neary] = 1
                total += board[nearx][neary]
                queue.append((nearx, neary))
    idx += 1

print(total)
