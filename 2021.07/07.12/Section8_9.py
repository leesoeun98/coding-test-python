n, m = map(int, input().split())
dp=[0]*(m+1)
jewels=[]
for _ in range(n):
    jewels.append(list(map(int, input().split())))
jewels.sort()
for i in range(1, m+1):
    for j in range(n):
        if i>=jewels[j][0]:
            dp[i]=max(dp[i], dp[i-jewels[j][0]]+jewels[j][1])
print(dp[m])