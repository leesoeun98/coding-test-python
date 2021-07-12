n = int(input())
num=[0]+list(map(int, input().split()))
dp=[1]*(n+1)
#게속 증가해야 최대이므로, 최대 증가 수열과 같은 문제
for i in range(1, n+1):
    for j in range(1, i):
        if num[i]>num[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(max(dp))