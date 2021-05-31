from collections import deque

a, b, c = map(int, input().split())
queue = deque()
visited = [[0] * 201 for _ in range(201)]
ans = []
queue.append([0, 0, c])
while queue:
    x, y, z = queue.popleft()
    if visited[x][y] == 1:
        continue
    visited[x][y] = 1
    if x == 0:
        ans.append(z)
    # a -> b or a 비우기
    if x + y > b:
        queue.append([x + y - b, b, z])
    else:
        queue.append([0, x + y, z])
    # a -> c or a 비우기
    if x + z > c:
        queue.append([x + z - c, y, c])
    else:
        queue.append([0, y, x + z])
    # b -> a or b 비우기
    if x + y > a:
        queue.append([a, x + y - a, z])
    else:
        queue.append([x + y, 0, z])
    # b -> c or b 비우기
    if y + z > c:
        queue.append([x, y + z - c, c])
    else:
        queue.append([x, 0, y + z])
    # c -> a or c 비우기
    if x + z > a:
        queue.append([a, y, z + x - a])
    else:
        queue.append([x + z, y, 0])
    # c -> b or c 비우기
    if y + z > b:
        queue.append([x, b, y + z - b])
    else:
        queue.append([x, y + z, 0])
ans.sort()
print(*ans)