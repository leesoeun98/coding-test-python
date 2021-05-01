n, m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
res=[0 for i in range(m)]
check=[0 for i in range(n)]
answer=[]
def DFS(depth):
    global answer
    if depth==m:
        answer.append(tuple(res.copy()))
        return
    else:
        for i in range(n):
            if check[i]==0:
                res[depth]=num[i]
                check[i]=1
                DFS(depth+1)
                check[i]=0
DFS(0)
for li in sorted(list(set(answer))):
    print(*li)