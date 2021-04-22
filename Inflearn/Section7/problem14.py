"""
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
maxh=-987654321
queue=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]>maxh:
            maxh=board[i][j]
answer=0
for rain in range(maxh):
    count=0
    check = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
                if board[i][j]>rain and check[i][j]==0:
                    check[i][j]=1
                    queue.append((i, j))
                    while queue:
                        x, y =queue.popleft()
                        for direction in range(4):
                            nearx=x+xd[direction]
                            neary=y+yd[direction]
                            if 0<=nearx<n and 0<=neary<n and board[nearx][neary]>rain and check[nearx][neary]==0:
                                check[nearx][neary]=1
                                queue.append((nearx, neary))
                    count+=1
    answer=max(answer, count)

print(answer)
"""
n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
answer=0
count=0

def DFS(i, j, height):
    check[i][j]=1
    for direction in range(4):
        nearx=i+xd[direction]
        neary=j+yd[direction]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]>height and check[nearx][neary]==0:
            DFS(nearx, neary, height)

for height in range(100):
    #비의양마다 count, check 새로 초기화 해야 함
    count=0
    check = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j]==0 and board[i][j]>height:
                #안전영역의 시작 DFS끝나면 안전영역도 끝
                count+=1
                DFS(i, j, height)
    #DFS끝나면 안전영역 개수들이 나옴
    answer=max(answer, count)
    if count==0:
        break
print(answer)

