n = int(input())
brick = []
for _ in range(n):
    area, height, weight = map(int, input().split())
    brick.append((area, height, weight))
dp = [0 for i in range(n)]
dp[0]=brick[0][1]
#무거운거 부터
brick.sort(reverse=True)

for i in range(n):
    max_h=0
    for j in range(i-1, -1, -1):
        #dp[j] 중 최대가 max_h이고 dp[i]=max_h+brick[i][1]
        if brick[j][2]>brick[i][2] and dp[j]>max_h:
            max_h=dp[j]
    dp[i]=max_h+brick[i][1]
print(max(dp))
