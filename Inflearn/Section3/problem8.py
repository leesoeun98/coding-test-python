#1차 시도 실패
#2차 성공
import sys

n= int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for t in range(int(input())):
    row, direction, cnt = map(int, input().split())
    if direction==0:
        for c in range(cnt):
            temp = board[row-1][0];
            for i in range(1, len(board[row-1])):
                board[row-1][i - 1] = board[row-1][i]
            board[row-1][len(board[row-1])-1] = temp
    else:
        for c in range(cnt):
            temp= board[row-1][len(board[row-1])-1]
            for i in range(len(board[row-1])-1, 0, -1):
                board[row-1][i]=board[row-1][i-1]
            board[row-1][0]=temp
mid=n//2
count=0
for i in range(n//2+1):
    for j in range(mid-(n//2-i), mid+(n//2-i)+1):
        count+=board[i][j]
for i in range(n//2+1, n):
    for j in range(mid-(i-n//2), mid+(i-n//2)+1):
        count+=board[i][j]
print(count)

