import sys
sys.setrecursionlimit(10**6)
x=[1,1,1,0,-1,-1,-1,0]
y=[1,0,-1,-1,-1,0,1,1]

def dfs(i, j):
    for d in range(8):
        nearx=x[d]+i
        neary=y[d]+j
        if 0<=nearx<h and 0<=neary<w and board[nearx][neary]==1:
            board[nearx][neary]=0
            dfs(nearx, neary)
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    else:
        board=[list(map(int, input().split())) for _ in range(h)]
        cnt=0
        for i in range(h):
            for j in range(w):
                if board[i][j]==1:
                    board[i][j]=0
                    dfs(i, j)
                    cnt+=1
        print(cnt)
