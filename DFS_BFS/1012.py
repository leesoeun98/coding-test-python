directionx=[-1,1,0,0] #4방향중 x축
directiony=[0,0,-1,1] #4방향중 y축

def DFS(i, j):
    # ground 전체에서 1을 확인 -> visted에 1로
    visited[i][j]=1
    for direction in range(4):
        # 동서남북 인접한 곳에 1이 있는지 확인 -> 재귀호출로 visted에 숫자넣기
        # 인접한 곳에 1 더이상 없으면 다음 전체 graph에서 1 확인
        nearx=i+directionx[direction]
        neary=j+directiony[direction]
        if 0<=nearx<m and 0<=neary<n:
            if ground[nearx][neary]==1 and visited[nearx][neary]==0:
                DFS(nearx, neary)

#입력 및 땅, 배추 세팅 + 함수 호출 및 답안출력
count=int(input())
for _ in range(count):
    m,n,k=map(int, input().split())
    ground=[[0]*(n) for i in range(m)]
    visited=[[0]*(n) for i in range(m)]
    for _ in range(k):
        x, y=map(int, input().split())
        ground[x][y]=1
    nums=0 #벌레 수
    for i in range(m):
        for j in range(n):
            if ground[i][j]==1 and visited[i][j]==0:
                DFS(i, j)
                nums+=1 #DFS 한번 끝나면 벌레 1증가

    print(nums)


