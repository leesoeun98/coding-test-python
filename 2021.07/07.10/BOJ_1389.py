from collections import deque
n,m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(start):
    queue=deque()
    distance=[0]*(n+1)
    visited[start]=1
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for adj in graph[cur]:
            if visited[adj]==0:
                visited[adj]=1
                distance[adj]=distance[cur]+1
                queue.append(adj)
    return sum(distance)

res=[]
for i in range(1, n+1):
    visited=[0]*(n+1)
    res.append(bfs(i))
print(res.index(min(res))+1)

