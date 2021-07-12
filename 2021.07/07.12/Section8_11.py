n, m = map(int, input().split())
problems=[]
dp=[0]*(m+1)

for _ in range(n):
    s, t = map(int, input().split())
    for j in range(m, t-1, -1):
        dp[j]=max(dp[j], dp[j-t]+s)
print(dp[m])