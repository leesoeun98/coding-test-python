n, m=map(int, input().split())
visited=[[0]*m for _ in range(n)]
# []로 선언 주의
maps=[]
for i in range(n):
    maps.append(list(list(map(int, input()))))
nums=1
directionx=[-1,1,0,0] #4방향중 x축
directiony=[0,0,-1,1] #4방향중 y축

queue=[(0,0)]
visited[0][0]=1
while queue:
    x, y=queue.pop(0) #pop(0)이므로 제일 왼쪽거가 pop
    if x==n-1 and y==m-1:
        print(visited[x][y])
        break
    #현 node의 4방향 인접노드에서
    for i in range(4):
        # 인접한 노드들 중에서 (4방향으로 탐색) 범위 내에 있고 해당 좌표가 1이라면
        nearx=x+directionx[i]
        neary=y+directiony[i]
        #여기서는 n, m 거꾸로 주의
        if 0<=nearx<n and 0<=neary<m:
            if maps[nearx][neary]==1 and visited[nearx][neary]==0:
                queue.append((nearx, neary))
                #칸 수를 visited에 저장
                visited[nearx][neary]=1+visited[x][y]