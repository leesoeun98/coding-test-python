from collections import deque
import sys
n = int(input())
tree = {}
parents = [0] * (n + 1)
queue = deque()
queue.append(1)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a] = tree.get(a, []) + [b]
    tree[b] = tree.get(b, []) + [a]


while queue:
    node = queue.popleft()
    for next in tree[node]:
        if parents[node]!=next:
            parents[next]=node
            queue.append(next)

for i in range(2, n+1):
    print(parents[i])