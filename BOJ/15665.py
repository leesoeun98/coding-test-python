n, m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
res=[0 for i in range(m)]
answer=[]

def DFS(depth):
    if depth==m:
        answer.append(tuple(res))
        return
    else:
        for i in range(n):
            res[depth]=num[i]
            DFS(depth+1)
DFS(0)
answer=sorted(list(set(answer)))
for a in answer:
    print(*a)