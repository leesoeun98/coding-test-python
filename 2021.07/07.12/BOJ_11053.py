n = int(input())
num=list(map(int, input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(max(dp))