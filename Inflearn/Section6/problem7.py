n = int(input())
coins=list(map(int, input().split()))
coins.sort(reverse=True)
change=int(input())
dp=[0 for i in range(change+1)]
#초기화 주의....1부터 끝까지 해야 맨 초반에 min값이 0됨
for i in range(1, change+1):
    dp[i]=987654321
for i in range(n):
    for j in range(coins[i], change+1):
        dp[j]=min(dp[j], dp[j-coins[i]]+1)
print(dp[change])