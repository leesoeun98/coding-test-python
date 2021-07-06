import sys
sys.setrecursionlimit(10**6)
def dfs(node, visited):
    visited+=[node]
    next=num[node]
    if next not in visited:
        check[next]=1
        dfs(next, visited)
    elif next==visited[0]:
        return visited

for _ in range(int(input())):
    n=int(input())
    num=[0]+list(map(int, input().split()))
    check=[0]*(n+1)
    cnt=0
    for i in range(1, n+1):
        if check[i]==0:
            dfs(i, [])
            cnt+=1
    print(cnt)