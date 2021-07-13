from collections import deque
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node, visited):
    for next in range(len(graph[node])):
        if next not in visited and graph[node][next]==1:
            visited+=[next]
            dfs(next, visited)
    return visited

def bfs(start):
    queue=deque()
    queue.append(start)
    visited=[start]
    while queue:
        cur = queue.popleft()
        for next in range(len(graph[cur])):
            if graph[cur][next]==1 and next not in visited:
                visited+=[next]
                queue.append(next)
    return visited

print(*(dfs(v, [v])))
print(*bfs(v))