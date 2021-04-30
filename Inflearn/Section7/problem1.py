n, m = map(int, input().split())
problems = []
for i in range(n):
    score, time = map(int, input().split())
    problems.append((score, time))
res = -987654321


def DFS(depth, sumscore, sumtime):
    global res
    if sumtime > m:
        return
    if depth == n:
        #m보다 작거나 같으면 됨 주의
        if sumtime <= m:
            if res < sumscore:
                res = sumscore
        return
    else:
        # 문제 풀 때
        DFS(depth + 1, sumscore + problems[depth][0], sumtime + problems[depth][1])
        # 문제 안 풀 때
        DFS(depth + 1, sumscore, sumtime)


DFS(0, 0, 0)
print(res)
