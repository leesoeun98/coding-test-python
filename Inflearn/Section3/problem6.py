import sys
n = int(input())
board=[]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
answer=[]

for j in range(n):
    sum=0
    for i in range(n):
        sum+=board[i][j]
    answer.append(sum)

for i in range(n):
    sum=0
    for j in range(n):
        sum+=board[i][j]
    answer.append(sum)
sum=0
for i in range(n):
    sum+=board[i][i]
answer.append(sum)

print(max(answer))