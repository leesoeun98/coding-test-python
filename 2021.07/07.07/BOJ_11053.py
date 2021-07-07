n = int(input())
dp = [1] * n
num = list(map(int, input().split()))
for i in range(n):
    for j in range(i):
        if num[i]>num[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))