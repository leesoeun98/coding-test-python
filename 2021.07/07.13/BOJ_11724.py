import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)


def dfs(node, check):
    for next in graph[node]:
        if next not in check and visited[next] == 0:
            check += [next]
            visited[next] = 1
            dfs(next, check)
    return


cnt = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i, [i])
        cnt += 1
print(cnt)
