n=int(input())
coins=list(map(int, input().split()))
m=int(input())
dp=[987654321]*(m+1)
coins.sort()
dp[0]=0

for i in range(coins[0], m+1):
    for j in range(len(coins)):
        dp[i]=min(dp[i], dp[i-coins[j]]+1)
print(dp[m])