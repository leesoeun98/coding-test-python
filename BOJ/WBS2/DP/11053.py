# 수열의 끝을 구하는게 아니라 최댓값을 찾는거임 주의
n = int(input())
num = list(map(int, input().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if num[j] < num[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
