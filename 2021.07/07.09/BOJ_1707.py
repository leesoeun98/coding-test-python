import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, color):
    global flag
    visited[node] = color
    for adj in graph[node]:
        if visited[adj] == color:
            flag = False
            return
        if visited[adj]==0:
            dfs(adj, -color)


for _ in range(int(input())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    flag = True
    for i in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    for i in range(1, v + 1):
        if not flag:
            break
        if visited[i] == 0:
            dfs(i, 1)
    if flag:
        print("YES")
    else:
        print("NO")
