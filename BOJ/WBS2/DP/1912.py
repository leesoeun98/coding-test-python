n = int(input())
num = list(map(int, input().split()))
dp = [x for x in num]
for i in range(1, n):
    # num[i] 랑 dp[i-1]+num[i]중 최대 비교
    dp[i] = max(dp[i], dp[i - 1] + num[i])
print(max(dp))
