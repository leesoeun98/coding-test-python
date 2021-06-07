n = int(input())
bridge=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
def DFS(x, y):
    if dp[x][y]>0:
        return dp[x][y]
    elif x==0 and y==0:
        return bridge[0][0]
    else:
        if x==0:
            dp[x][y]=DFS(x, y-1)+bridge[x][y]
        elif y==0:
            dp[x][y]=DFS(x-1, y)+bridge[x][y]
        else:
            dp[x][y]=min(DFS(x-1, y), DFS(x, y-1))+bridge[x][y]
        return dp[x][y]

print(DFS(n-1, n-1))