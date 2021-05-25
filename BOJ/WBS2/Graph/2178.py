from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

distance = [[0] * m for _ in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
queue = deque()
#시작점이 정해졌으니 이거만 넣어주면 됨 for문 아님!!
queue.append((0, 0))

# 최소 칸 수로 가야 함 =>dfs는 보장하지 않음. bfs로 해야함
while queue:
    x, y = queue.popleft()
    for direction in range(4):
        nearx = x + xd[direction]
        neary = y + yd[direction]
        if 0 <= nearx < n and 0 <= neary < m and maze[nearx][neary] == 1 and distance[nearx][neary] == 0:
            distance[nearx][neary] = distance[x][y] + 1
            queue.append((nearx, neary))
print(distance[n-1][m-1]+1)
