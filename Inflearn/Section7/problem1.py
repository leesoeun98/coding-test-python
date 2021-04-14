n, m = map(int, input().split())
problems=[]
res=0
for _ in range(n):
    score, time = map(int, input().split())
    problems.append((score, time))
def DFS(p, score, time):
    global res
    if p==n:
        if time<=m:
            res=max(res, score)
        return
    elif time == m:
        res=max(res, score)
        return
    else:
        #문제 풀었을 때
        DFS(p+1, score+problems[p][0], time+problems[p][1])
        #문제 못 풀었을 때
        DFS(p+1, score, time)
DFS(0,0,0)
print(res)
