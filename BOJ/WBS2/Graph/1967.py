from collections import deque

n = int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, d = map(int, input().split())
    tree[p].append([d, c])
    tree[c].append([d, p])

# root인 1에서 가장 먼 노드 구하기
# 해당 노드에서 가장 먼 노드까지의 거리 구하기
def bfs(root, mode):
    queue=deque()
    queue.append(root)
    distance=[-1 for _ in range(n+1)]
    distance[root]=0

    while queue:
        node = queue.popleft()
        for d, adj in tree[node]:
            if distance[adj]==-1:
                distance[adj]=distance[node]+d
                queue.append(adj)
    if mode==1:
        return distance.index(max(distance))
    else:
        return max(distance)

print(bfs(bfs(1,1), 0))