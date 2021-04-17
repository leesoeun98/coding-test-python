# 시간초과 => 백트래킹 필요
c, n = map(int, input().split())
weight = []
result = -987654321
for i in range(n):
    weight.append(int(input()))
total = sum(weight)


def DFS(depth, curweight, checksum):
    global result
    # 누적합을 기록해서 전체-누적합이 (앞으로 탐색 남은 애들)+현재 sum이 res보다 작으면 탐색할 이유 x
    if curweight + (total - checksum) < result:
        return
    if curweight > c:
        return
    if depth == n:
        if result < curweight:
            result = curweight
        return
    else:
        DFS(depth + 1, curweight + weight[depth], checksum + weight[depth])
        DFS(depth + 1, curweight, checksum + weight[depth])


DFS(0, 0, 0)
print(result)
