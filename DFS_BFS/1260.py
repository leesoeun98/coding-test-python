from _collections import deque
n,m,v=map(int, input().split())
graph=[[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    start, end=map(int, input().split())
    #양방향이므로 양쪽에 1을 넣음
    graph[start][end]=1
    graph[end][start]=1


def DFS(current_node,graph, visited):
    visited+=[current_node]
    for search_node in range(len(graph[current_node])):
    #현 node의 그래프 길이 만큼 반복 + dfs는 깊이 탐색해야하므로 재귀이용
        if graph[current_node][search_node] and search_node not in visited:
            #자식 노드까지 모두 탐색하게 current_node에 search_node넣어서 재귀 호출
            DFS(search_node, graph, visited)
    return visited

def BFS(graph, root):
    queue=[root]
    visited=[root]
    while queue:
        current_node=queue.pop(0) #pop(0)이므로 제일 왼쪽거가 pop
        for search_node in range(len(graph[current_node])):
            #현 node의 그래프 길이 만큼 반복
           if graph[current_node][search_node] and search_node not in visited:
            #graph[current_node][search_node]는 0또는 1-> 간선이 있으면 1
            #즉, 간선이 있고 search_node를 방문 안했다면 방문한걸로 바꾸고 queue에 넣음
               queue+=[search_node]
               visited+=[search_node]
    return visited

print(*DFS(v,graph , []))
#*은 리스트 unpacking 연산자
print(*BFS(graph, v))