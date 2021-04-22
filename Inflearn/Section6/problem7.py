n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
m = int(input())
res = 987654321


def DFS(depth, change):
    global res
    # res보다 동전개수 많이 쓸 경우 탐색할 필요 x
    if depth > res:
        return
    if change > m:
        return
    # 금액이 m이 되면 종료
    # m이 될떼까지 depth가 곧 동전 개수
    # 동전 n개 가지 뻗고 다시 n개 뻗고의 반복이라 for문 사용
    if change == m:
        if res > depth:
            res = depth
        return
    else:
        for i in range(n):
            DFS(depth + 1, change + coin[i])


DFS(0, 0)
print(res)

"""n = int(input())
coins=list(map(int, input().split()))
coins.sort(reverse=True)
change=int(input())
dp=[0 for i in range(change+1)]
#초기화 주의....1부터 끝까지 해야 맨 초반에 min값이 0됨
for i in range(1, change+1):
    dp[i]=987654321
for i in range(n):
    for j in range(coins[i], change+1):
        dp[j]=min(dp[j], dp[j-coins[i]]+1)
print(dp[change])"""
