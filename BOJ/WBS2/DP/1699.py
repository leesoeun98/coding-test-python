#방향은 맞으나 인덱싱이나, 코드 구현력에서 부족함
n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = i
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - (j * j)] + 1
print(dp[n])
