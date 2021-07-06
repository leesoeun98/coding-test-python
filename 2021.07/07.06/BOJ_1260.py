from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1
queue=deque()

def dfs(node, visited):
    visited += [node]
    for next in range(len(graph[node])):
        if graph[node][next]==1 and next not in visited:
            dfs(next, visited)
    return visited


def bfs():
    visited=[v]
    queue.append(v)
    while queue:
        cur = queue.popleft()
        for next in range(len(graph[cur])):
            if graph[cur][next]==1 and next not in visited:
                visited += [next]
                queue.append(next)
    return visited


print(*dfs(v, []))
print(*bfs())
