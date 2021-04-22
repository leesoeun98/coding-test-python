n, m = map(int, input().split())
check = [False for i in range(n)]
res = [0 for i in range(m)]
count = 0


def DFS(depth):
    global count
    if depth == m:
        print(*res)
        count += 1
        return
    else:
        # n개의 가지를 뻗고 다시 또 뻗을거라 for문
        for i in range(n):
            if not check[i]:
                res[depth] = i + 1
                check[i] = True
                DFS(depth + 1)
                # 원상복귀
                check[i] = False


DFS(0)
print(count)
