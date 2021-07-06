for _ in range(int(input())):
    dp=[1,1,1,2,2]
    n=int(input())
    for i in range(4,n):
        dp.append(dp[i]+dp[i-4])
    print(dp[n-1])