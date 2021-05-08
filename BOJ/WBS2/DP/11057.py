dp = [[0] * 10 for i in range(1001)]
n = int(input())
for i in range(10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][:j + 1])
print(sum(dp[n])%10007)
