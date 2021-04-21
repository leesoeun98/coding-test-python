c, n = map(int, input().split())
dogs = []
res = -987654321
for i in range(n):
    dogs.append(int(input()))
# total 위치 주의
total = sum(dogs)


def DFS(depth, sumw, p):
    global res
    if sumw + (total - p) < res:
        return
    if sumw > c:
        return
    if depth == n:
        if sumw > res:
            res = sumw
        return
    else:
        # 넣고 + 앞으로 탐색할 강아지들+sumw가 res보다 작으면 의미 업음
        DFS(depth + 1, sumw + dogs[depth], p + dogs[depth])
        # 안넣고
        DFS(depth + 1, sumw, p + dogs[depth])


DFS(0, 0, 0)
print(res)
