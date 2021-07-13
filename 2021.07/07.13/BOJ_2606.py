n = int(input())
m=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node, visited):
    visited+=[node]
    for next in tree[node]:
        if next not in visited:
            dfs(next, visited)
    return visited

print(len(dfs(1, []))-1)