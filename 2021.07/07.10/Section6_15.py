n, m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
cnt=0
def dfs(node, end, visited):
    global cnt
    if node==end:
        cnt+=1
    for adj in graph[node]:
        if adj not in visited:
            visited+=[adj]
            dfs(adj, end, visited)
            visited.pop()
dfs(1, n, [1])
print(cnt)