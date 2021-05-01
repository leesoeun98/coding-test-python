n, m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
res=[0 for i in range(m)]
answer=[]

def DFS(depth, start):
    if depth==m:
        answer.append(tuple(res))
        return
    else:
        for i in range(start, n):
            res[depth]=num[i]
            DFS(depth+1, i)
DFS(0, 0)
answer=sorted(list(set(answer)))
for a in answer:
    print(*a)