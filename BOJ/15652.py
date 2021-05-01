n, m = map(int, input().split())
res = [0 for i in range(m)]
check = [0 for i in range(n)]


def DFS(depth, start):
    if depth == m:
        print(*res)
        return
    else:
        for i in range(start, n):
            res[depth] = i + 1
            DFS(depth + 1, i)


DFS(0, 0)
