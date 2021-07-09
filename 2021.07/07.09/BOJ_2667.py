n = int(input())
board=[list(map(int, input())) for _ in range(n)]
xd=[-1,1,0,0]
yd=[0,0,-1,1]
idx=2
res=[]
def dfs(i, j):
    global cnt
    for d in range(4):
        nearx=i+xd[d]
        neary=j+yd[d]
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]==1:
            cnt+=1
            board[nearx][neary]=idx
            dfs(nearx, neary)

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            cnt=1
            board[i][j]=idx
            dfs(i, j)
            res.append(cnt)
print(len(res))
res.sort()
for r in res:
    print(r)
