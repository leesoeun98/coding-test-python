from collections import deque

v = int(input())
tree = [[] * (v + 1)]
for _ in range(v - 1):
    p, c, w = map(int, input().split())
    tree[p].append([c, w])
    tree[c].append([p, w])


def bfs(root, mode):
    queue = deque()
    queue.append(root)
    distance = [-1] * (v + 1)
    distance[root] = 0

    while queue:
        node = queue.popleft()
        for adj, w in tree[node]:
            if distance[adj] == -1:
                distance[adj] = distance[node] + w
                queue.append(adj)
    if mode == 1:
        return distance.index(max(distance))
    else:
        return max(distance)


print(bfs(bfs(1, 1), 0))
