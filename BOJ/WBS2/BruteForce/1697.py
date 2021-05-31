from collections import deque

n, k = map(int, input().split())
visited = [0 for i in range(100001)]
queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft()
    if cur == k:
        print(visited[cur])
        break
    if 0 <= cur - 1 <= 100000 and visited[cur - 1] == 0:
        visited[cur - 1] = visited[cur] + 1
        queue.append(cur - 1)
    if 0 <= cur + 1 <= 100000 and visited[cur + 1] == 0:
        visited[cur + 1] = visited[cur] + 1
        queue.append(cur + 1)
    if 0 <= cur * 2 <= 100000 and visited[cur * 2] == 0:
        visited[cur * 2] = visited[cur] + 1
        queue.append(cur*2)
