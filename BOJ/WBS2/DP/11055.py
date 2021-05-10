n = int(input())
num = list(map(int, input().split()))
dp = [num[i] for i in range(n)]
before = dp[0]
for i in range(n):
    for j in range(i):
        if num[i] > num[j] and dp[i] < dp[j] + num[i]:
            dp[i] = dp[j] + num[i]
print(max(dp))
