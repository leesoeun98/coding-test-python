import sys
n = int(input())
board=[]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

largest =-2147000000
for j in range(n):
    sum1=sum2=0
    for i in range(n):
        sum1+=board[i][j]
        sum2+=board[j][i]
    largest = max(largest, sum1, sum2)

sum1=sum2=0
for i in range(n):
    sum1+=board[i][i]
    sum2+=board[i][n-i-1]
largest = max(largest, sum1, sum2)

print(largest)