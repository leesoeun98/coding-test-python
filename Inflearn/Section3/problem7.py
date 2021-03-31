import sys

n= int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mid=n//2
count=0
for i in range(n//2+1):
    for j in range(mid-i, mid+i+1):
        count+=board[i][j]
for i in range(n//2+1, n):
    for j in range(mid-(n-1-i), mid+(n-i-1)+1):
        count+=board[i][j]
print(count)