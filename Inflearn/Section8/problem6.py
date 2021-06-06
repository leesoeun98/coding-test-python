n = int(input())
right=list(map(int, input().split()))
dp=[1 for _ in range(n+1)]

#왼쪽이 증가이므로 오른쪽에서도 증가수열이어야 교차하지 않음
# -> 최대 증가 수열 문제임
for i in range(n):
    for j in range(i):
        if right[j]<right[i] and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1
print(max(dp))