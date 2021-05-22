from collections import deque

# dict 대신에 2차원 matrix 쓰자 (간선 여러개면 갱신해줘야하므로)
n, m, v = map(int, input().split())
matrix=[[0]*(n+1) for _ in range(n+1)]
queue = deque()

for i in range(m):
    start, end = map(int, input().split())
    matrix[start][end]=1
    matrix[end][start]=1


def BFS(node):
    visited=[node]
    queue.append(node)
    while queue:
        node = queue.popleft()
        for i in range(len(matrix[node])):
            if matrix[node][i]==1 and (i not in visited):
                queue.append(i)
                visited.append(i)
    return visited


# dfs 다시 해보기
def DFS(node, visited):
    visited += [node]
    for i in range(len(matrix[node])):
        if matrix[node][i]==1 and (i not in visited):
            DFS(i, visited)
    return visited

#출력 주의
print(*DFS(v, []))
print(*BFS(v))
