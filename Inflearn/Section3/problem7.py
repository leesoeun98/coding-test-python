import sys
n = int(input())
board=[]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
sum=0
for i in range(n//2+1):
    for j in range(n//2-i, n//2+i+1):
        sum+=board[i][j]
for i in range(n//2+1, n):
    for j in range(n//2-(n-1-i), n//2+(n-1-i)+1):
        sum+=board[i][j]
print(sum)