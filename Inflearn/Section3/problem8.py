#1차 시도 실패 
import sys
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
m = int(input())
for _ in range(m):
    row, LR, count = map(int, input().split())
    items = deque(board[row - 1])
    if LR == 0:
        board[row - 1][:] = items.rotate(count)
    else:
        board[row - 1][:] = items.rotate(count)

sum = 0
for i in range(n // 2 + 1):
    for j in range(i, n // 2 + (n // 2 - i) + 1):
        sum += board[i][j]
for i in range(n // 2 + 1, n):
    for j in range(n // 2 - (i - n // 2), n // 2 + (i - n // 2) + 1):
        sum += board[i][j]
print(sum)
print(board)
