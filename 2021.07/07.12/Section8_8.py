n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]

def dfs(i, j):
    if dp[i][j]>0:
        return dp[i][j]
    elif i==0 and j==0:
        return board[0][0]
    else:
        if i==0:
            dp[i][j]=dfs(i, j-1)+board[i][j]
        elif j==0:
            dp[i][j]=dfs(i-1,j)+board[i][j]
        else:
            dp[i][j]=min(dfs(i-1,j), dfs(i,j-1))+board[i][j]
        return dp[i][j]

print(dfs(n-1, n-1))