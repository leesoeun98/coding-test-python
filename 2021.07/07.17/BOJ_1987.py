from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]

answer=1

def bfs(i, j):
    global answer
    queue=set([(i, j, board[i][j])])

    while queue:
        x, y, ans= queue.pop()
        for d in range(4):
            nx = x + xd[d]
            ny = y + yd[d]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in ans:
                queue.add((nx, ny, ans+board[nx][ny]))
                answer=max(answer, len(ans)+1)

bfs(0,0)
print(answer)