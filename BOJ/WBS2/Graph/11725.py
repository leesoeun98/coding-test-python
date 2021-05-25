from collections import deque
import sys
n = int(input())
#dict로 구성
graph = {}
parents=[0]*(n+1)
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x] = graph.get(x, []) + [y]
    graph[y] = graph.get(y, []) + [x]
queue=deque()
queue.append(1)

while queue:
    node = queue.popleft()
    #node 랑 연결된 것은 node의 부모거나 자식 중 하나
    for adj in graph[node]:
    #node의 부모가 아니면 자식 (node가 부모라는 소리)
        if parents[node]!=adj:
            parents[adj]=node
            queue.append(adj)

for i in range(2, len(parents)):
    print(parents[i])