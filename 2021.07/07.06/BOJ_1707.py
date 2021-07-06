import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, color):
    global flag
    bipartite[node]=color
    for next in graph[node]:
        if bipartite[next] == color:
            flag = False
            return
        if bipartite[next] == 0:
            dfs(next, -color)


for _ in range(int(input())):
    v, e = map(int, sys.stdin.readline().split())
    graph=[[] for _ in range(v+1)]
    bipartite=[0]*(v+1)
    flag=True
    for _ in range(e):
        start, end= map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    for i in range(1, v+1):
        if not flag:
            break
        if bipartite[i]==0:
            dfs(i, 1)
    if flag:
        print("YES")
    else:
        print("NO")

