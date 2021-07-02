import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        # 아직 방문 안했으면 다른 그룹에 넣고
        # 다른 그룹이 아니면 false
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        # 방문했는데 같은 그룹이면 false
        elif visited[i] == visited[v]:
            return False
    return True


for t in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    visited = [0] * (v + 1)
    for i in range(e):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)
    # 이분 그래프 여부 판별하는 flag
    bipatite = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')

"""
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, color):
    global flag
    check[node]=color
    for next in graph[node]:
        if check[next]==color:
            flag=False
            return
        if check[next]==0:
            dfs(next, -color)


for _ in range(int(input())):
    v, e = map(int, sys.stdin.readline().split())
    graph=[[] for _ in range(v+1)]
    check=[0]*(v+1)
    flag = True
    for _ in range(e):
        start, end=map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    for i in range(1, v+1):
        if not flag:
            break
        if check[i]==0:
            dfs(i, 1)
    if flag:
        print("YES")
    else:
        print("NO")

"""