import sys

n = int(input())
board = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n + 1):
        board[i][j] = arr[j - 1]

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
count=0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        flag = True
        for direction in range(4):
            nearx = x[direction] + i
            neary = y[direction] + j
            if 0 <= nearx <= n + 1 and 0 <= neary <= n + 1:
               if board[i][j] > board[nearx][neary]:
                   flag = True
               else:
                   flag = False
                   break
        if flag:
            count+=1
print(count)

"""
n= int(input())
board=[[0 for i in range(n+2)] for i in range(n+2)]
x=[-1, 1, 0, 0]
y=[0,0,1,-1]
count=0
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        board[i+1][j+1]=num[j]
for i in range(1, n+1):
    for j in range(1, n+1):
        for direction in range(4):
            nearx=x[direction]+i
            neary = y[direction]+j
            if board[i][j]<=board[nearx][neary]:
                break
        else:
            count+=1
print(count)
"""