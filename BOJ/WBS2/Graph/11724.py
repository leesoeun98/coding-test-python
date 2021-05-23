import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

n, m = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
check=[0]*(n+1)
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    matrix[start][end] = 1
    matrix[end][start] = 1
# 연결 요소란 DFS나 BFS로 탐색시 끊어지지 않고 탐색한 횟수
def DFS(start, visited):
    visited.add(start)
    for end in range(len(matrix[start])):
        if matrix[start][end]==1 and end not in visited:
            DFS(end, visited)
            check[end]=1
count=0
for i in range(1, n+1):
    if check[i]==0:
        visited=set()
        DFS(i, visited)
        count+=1
print(count)