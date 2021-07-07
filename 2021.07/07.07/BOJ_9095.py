for _ in range(int(input())):
    n=int(input())
    dp = [1, 2, 4]
    for i in range(2, n+1):
        dp.append(dp[i]+dp[i-1]+dp[i-2])
    print(dp[n-1])
