k = int(input())
weight=list(map(int, input().split()))
res=set()
def dfs(depth, sumw):
    if depth==k:
        if sumw>0:
            res.add(sumw)
        return
    else:
        #왼
        dfs(depth+1, sumw-weight[depth])
        #오
        dfs(depth+1, sumw+weight[depth])
        #안 넣기
        dfs(depth+1, sumw)

dfs(0,0)
print(sum(weight)-len(res))