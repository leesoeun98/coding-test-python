n = int(input())
scores = [0]
for _ in range(n):
    scores.append(int(input()))
dp = [0, scores[1]]
if n > 1:
    dp.append(max(scores[1] + scores[2], scores[0] + scores[2]))
# 마지막 계단을 꼭 밟아야 하므로 scores[i]는 꼭 들어가야 함
for i in range(3, n + 1):
    dp.append(max(scores[i] + scores[i - 1] + dp[i - 3], scores[i] + dp[i - 2]))
print(dp[n])
