from collections import deque
n = int(input())
board=[list(map(int, input().split())) for i in range(n)]
check=[[0]*n for i in range(n)]
count=0
mid=n//2
xd=[-1, 1, 0, 0]
yd=[0, 0, 1, -1]
#초기화
queue=deque()
queue.append((mid, mid))
check[mid][mid]=1
count+=board[mid][mid]
index=0
while True:
    if index==n//2:
        break
    for i in range(len(queue)):
        x, y = queue.popleft()
        for direction in range(4):
            nearx=x+xd[direction]
            neary=y+yd[direction]
            if 0<=nearx<=n-1 and 0<=neary<=n-1:
                if check[nearx][neary]==0:
                    count+=board[nearx][neary]
                    check[nearx][neary]=1
                    queue.append((nearx, neary))
    index+=1
print(count)
