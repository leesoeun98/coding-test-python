import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
graph=[[0]*(n+1) for _ in range(n+1)]
check=[0]*(n+1)
for _ in range(m):
    start, end=map(int, sys.stdin.readline().split())
    graph[start][end]=1
    graph[end][start]=1

def dfs(node, visited):
    visited+=[node]
    for next in range(len(graph[node])):
        if graph[node][next]==1 and next not in visited:
            check[next]=1
            dfs(next, visited)
    return visited

cnt=0
for i in range(1, n+1):
    if check[i]==0:
        dfs(i, [])
        cnt+=1
print(cnt)


