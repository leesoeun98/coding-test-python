from collections import deque
xd = [0, 1, 1, 1, 0, -1, -1, -1]
yd = [1, 1, 0, -1, -1, -1, 0, 1]
n=int(input())
maps=[list(map(int, input().split())) for i in range(n)]
queue=deque()
#초기화 주의
count=0
for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            maps[i][j]=0
            queue.append((i, j))
            # queue 끝나면 섬도 끝남
            while queue:
                x, y=queue.popleft()
                for direction in range(8):
                    nearx=x+xd[direction]
                    neary=y+yd[direction]
                    if 0<=nearx<n and 0<=neary<n and maps[nearx][neary]==1:
                        maps[nearx][neary]=0
                        queue.append((nearx, neary))
            count+=1
print(count)
