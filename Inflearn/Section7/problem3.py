k = int(input())
weight = list(map(int, input().split()))
total = sum(weight)
check = set()


def DFS(depth, sumw):
    if depth == k:
        if 0 < sumw <= total:
            check.add(sumw)
        return
    else:
        # 안넣고
        DFS(depth + 1, sumw)
        # 왼쪽에 넣고
        DFS(depth + 1, sumw - weight[depth])
        # 오른쪽에 넣고
        DFS(depth + 1, sumw + weight[depth])


DFS(0, 0)
print(total - len(check))
