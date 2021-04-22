n, m = map(int, input().split())
adj = [[0 for i in range(n + 1)] for i in range(n + 1)]
check = [0 for i in range(n + 1)]
count = 0
for i in range(m):
    start, end = map(int, input().split())
    adj[start][end] = 1
path = []
# 초기화
path.append(1)
check[1] = 1


def DFS(depth):
    global count, path
    if depth == n:
        print(*path)
        count += 1
        return
    else:
        for i in range(1, n + 1):
            if adj[depth][i] == 1 and check[i] == 0:
                check[i] = 1
                path.append(i)
                DFS(i)
                # 원상복귀
                path.pop()
                check[i] = 0


DFS(1)
print(count)
