n = int(input())
num = list(map(int, input().split()))
dp = [1 for i in range(n)]
# i가 끝나는 지점, i보다 앞에 있는 j 애들이 더 커야 함
for i in range(n):
    for j in range(i):
        if num[j] > num[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
