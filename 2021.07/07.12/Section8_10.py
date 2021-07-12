n=int(input())
coins=list(map(int, input().split()))
m=int(input())
dp=[987654321]*(m+1)
dp[0]=0
for i in range(1, m+1):
    for j in range(n):
        if i>=coins[j]:
            dp[i]=min(dp[i],dp[i-coins[j]]+1)
print(dp[m])