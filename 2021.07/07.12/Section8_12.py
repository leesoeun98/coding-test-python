# 초기화 파트
n, m = map(int, input().split())
distance = [[5000] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    distance[i][i] = 0
for _ in range(m):
    s, e, d = map(int, input().split())
    distance[s][e] = d

# 플로이드-와샬 (순서 주의)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 출력파트
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j]==5000:
            print("M", end=" ")
        else:
            print(distance[i][j], end=" ")
    print()