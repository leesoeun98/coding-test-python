n = int(input())
dp = [0, 1, 3]
for i in range(3, n + 1):
    if i % 2 == 0:
        dp.append(1 + 2 * dp[i - 1])
    else:
        dp.append(2 * dp[i - 1] - 1)
print(dp[n] % 10007)
