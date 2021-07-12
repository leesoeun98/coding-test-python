for _ in range(int(input())):
    dp = [0, 1, 2, 4, 7]
    n=int(input())
    for i in range(4, n):
        dp.append(dp[i]+dp[i-1]+dp[i-2])
    print(dp[n])