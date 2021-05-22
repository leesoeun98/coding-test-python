import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다
def DFS(start,visited):
    visited+=[start]
    #어차피 1개만 연결됨
    next = matrix[start]
    if next not in visited:
        DFS(next, visited)
        check[next] = 1

for _ in range(int(input())):
    n = int(input())
    #초기화 문제 어차피 index랑 mapping이니까 앞에 0만 추가하면 1->3 2->4 이렇게 된다.
    matrix = [0]+list(map(int, input().split()))
    check=[0]*(n+1)
    count=0
    for i in range(1, n+1):
        if check[i]==0:
            DFS(i, [])
            count+=1
    print(count)

