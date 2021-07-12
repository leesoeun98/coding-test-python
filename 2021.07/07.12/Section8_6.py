n = int(input())
bricks=[]
for _ in range(n):
    bricks.append(list(map(int, input().split())))
dp=[0]*n
dp[0]=bricks[0][1]
bricks.sort(reverse=True)
for i in range(n):
    max_h=0
    for j in range(i-1, -1, -1):
        if bricks[j][2]>bricks[i][2] and max_h<dp[j]:
            max_h=dp[j]
    dp[i]=max_h+bricks[i][1]
print(dp)