import sys
sys.setrecursionlimit(10**6)
def dfs(node, color):
    global flag
    visited[node]=color
    for next in board[node]:
        if visited[next]==0:
            dfs(next, -color)
        if visited[next]==color:
            flag=False
            return

for _ in range(int(input())):
    v, e = map(int, sys.stdin.readline().split())
    board=[[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        board[a].append(b)
        board[b].append(a)
    flag=True
    visited=[0]*(v+1)
    for i in range(1, v+1):
        if not flag:
            break
        if visited[i]==0:
            dfs(i, 1)
    if flag:
        print("YES")
    else:
        print("NO")



