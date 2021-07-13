import sys
sys.setrecursionlimit(10**6)
n = int(input())
board=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]

def dfs(i, j):
    global cnt
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]==1:
            board[nearx][neary]=idx
            cnt+=1
            dfs(nearx, neary)
idx=2
res=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=idx
            cnt=1
            dfs(i, j)
            res.append(cnt)
            idx+=1
res.sort()
print(len(res))
for r in res:
    print(r)