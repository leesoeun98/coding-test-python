from collections import deque
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
n=int(input())
board=[list(map(int, input())) for i in range(n)]
res=[]
queue=deque()
# 전체 단지 다 돌아야 하므로 이중 for문 안에 queue
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            queue.append((i, j))
            count=1
            while queue:
                x, y=queue.popleft()
                for direction in range(4):
                    nearx=x+xd[direction]
                    neary=y+yd[direction]
                    if 0<=nearx<=n-1 and 0<=neary<=n-1 and board[nearx][neary]==1:
                        board[nearx][neary]=0
                        count+=1
                        queue.append((nearx, neary))
            res.append(count)
print(len(res))
res.sort()
print(*res)