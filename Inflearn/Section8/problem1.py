"""n = int(input())
dp=[0 for i in range(n+1)]
dp[1]=1
dp[2]=2
for i in range(3, n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])"""
n=int(input())

def Line(x):
    if x==1:
        return 1
    if x==2:
        return 2
    else:
        return Line(x-1)+Line(x-2)
print(Line(n))