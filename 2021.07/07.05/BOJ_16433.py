from collections import deque
n, r, c = map(int, input().split())
board = [['.'] * (n) for _ in range(n)]
queue=deque()
queue.append((r-1, c-1))
x = [1, 1, -1, -1]
y = [1, -1, -1, 1]

while queue:
    curx, cury=queue.popleft()
    for d in range(4):
        nearx=curx+x[d]
        neary=cury+y[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]=='.':
            board[nearx][neary]='v'
            queue.append((nearx, neary))
for line in board:
    print(''.join(line))

