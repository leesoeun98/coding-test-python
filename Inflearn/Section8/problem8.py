n = int(input())
bridge=[list(map(int, input().split())) for _ in range(n)]

# 각 좌표까지 도달하는데 걸린 에너지를 dp에 저잘
dp=[[987654321]*(n) for _ in range(n)]
dp[0][0]=bridge[0][0]

# 아래, 오른쪽 먼저 하고서 (여기는 왼쪽에서만 오거나 위에서만 올 수 있으므로)
for i in range(1, n):
    dp[0][i]=dp[0][i-1]+bridge[0][i]
    dp[i][0]=dp[i-1][0]+bridge[i][0]

# i, j는 이전거 + 현재 bridge i, j 값
for i in range(1, n):
    for j in range(1, n):
        dp[i][j]=min(dp[i-1][j], dp[i][j-1])+bridge[i][j]

print(dp[n-1][n-1])