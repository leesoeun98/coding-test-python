n, m = map(int, input().split())
problems = []
for i in range(n):
    score, time = map(int, input().split())
    problems.append((score, time))
res = -987654321


def DFS(depth, sumscore, sumtime):
    global res
    if depth == n:
        if res < sumscore and sumtime <= m:
            res = sumscore
        return
    if sumtime > m:
        return
    else:
        # 문제 풀고
        DFS(depth + 1, sumscore + problems[depth][0], sumtime + problems[depth][1])
        # 문제 안풀고
        DFS(depth + 1, sumscore, sumtime)


DFS(0, 0, 0)
print(res)
