dp=[0,1,1,1,2,2]
for i in range(6, 101):
    dp.append(dp[i-1]+dp[i-5])
for t in range(int(input())):
    print(dp[int(input())])


"""
for _ in range(int(input())):
    dp = [1, 1, 1, 2, 2]
    n=int(input())
    for i in range(4, n):
        dp.append(dp[i]+dp[i-4])
    print(dp[n-1])
"""