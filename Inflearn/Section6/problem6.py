n, m = map(int, input().split())
res = [0 for i in range(m)]
count = 0


def DFS(depth):
    global count
    if depth == m:
        print(*res)
        count += 1
        return
    else:
        # 가지 n개가 존재하고, 각 가지에서 다시 n개 뻗어나가니까 for문
        for i in range(n):
            # 이전에 뽑은거 중복가능해서 그냥 res에 넣고 depth만 증가시키면 됨
            res[depth] = i + 1
            DFS(depth + 1)


DFS(0)
print(count)
