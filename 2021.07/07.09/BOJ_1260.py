n, m, v = map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end=map(int, input().split())
    graph[start][end]=1
    graph[end][start]=1

def dfs(node, visited):
    for adj in range(len(graph[node])):
        if graph[node][adj]==1 and adj not in visited:
            visited+=[adj]
            dfs(adj, visited)
    return visited

def bfs(node):
    queue=[node]
    visited=[node]
    while queue:
        cur = queue.pop(0)
        for adj in range(len(graph[cur])):
            if graph[cur][adj]==1 and adj not in visited:
                visited+=[adj]
                queue.append(adj)
    return visited

print(*dfs(v, [v]))
print(*bfs(v))