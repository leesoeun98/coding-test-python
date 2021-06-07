n, m = map(int, input().split())
dp=[0]*(m+1)
jew=[]
for _ in range(n):
    w, p = map(int, input().split())
    jew.append((w, p))
jew.sort()

for i in range(1,m+1):
    for j in range(n):
        if i>=jew[j][0]:
            dp[i]=max(dp[i], dp[i-jew[j][0]]+jew[j][1])
print(dp[m])