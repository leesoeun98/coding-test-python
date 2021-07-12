from collections import deque
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
xd=[1,1,1,0,-1,-1,-1,0]
yd=[1,0,-1,-1,-1,0,1,1]
queue=deque()
cnt=0
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for d in range(8):
                    nearx=x+xd[d]
                    neary=y+yd[d]
                    if 0<=nearx<n and 0<=neary<n and board[nearx][neary]==1:
                        board[nearx][neary]=0
                        queue.append((nearx, neary))
            cnt+=1
print(cnt)
