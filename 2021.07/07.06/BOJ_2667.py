n = int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input())))

res=[]
x=[-1,1,0,0]
y=[0,0,-1,1]
def dfs(i, j):
    global cnt
    for d in range(4):
        nearx=x[d]+i
        neary=y[d]+j
        if 0<=nearx<n and 0<=neary<n and board[nearx][neary]==1:
            cnt+=1
            board[nearx][neary]=idx
            dfs(nearx, neary)


idx=2
for i in range(n):
    for j in range(n):
        cnt=1
        if board[i][j]==1:
            board[i][j]=idx
            dfs(i, j)
            res.append(cnt)
            idx+=1
res.sort()
print(len(res))
for r in res:
    print(r)