import sys
sys.setrecursionlimit(1000000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

def dfs(node, visited):
    global answer
    check[node]=1
    visited+=[node]
    next=students[node]
    if check[next]==1:
        if next in visited:
            answer+=visited[visited.index(next):]
            return
    else:
        dfs(next, visited)


for _ in range(int(input())):
    n=int(input())
    students=[0]+list(map(int, input().split()))
    check=[0]*(n+1)
    answer=[]
    for i in range(1, n+1):
        if check[i]==0:
            dfs(i, [])
    print(n-len(answer))


