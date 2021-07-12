from collections import deque
n, r, c = map(int, input().split())
xd=[1, 1, -1, -1]
yd=[1, -1, -1, 1]
board=[['.']*n for _ in range(n)]

queue=deque()
queue.append((r, c))
while queue:
    x, y = queue.popleft()
    for d in range(4):
        nearx=x+xd[d]
        neary=y+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]=='.':
            board[nearx][neary]='v'
            queue.append((nearx, neary))

for line in board:
    print(''.join(line))
