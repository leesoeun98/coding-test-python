c, n = map(int, input().split())
dogs=[]
for _ in range(n):
    dogs.append(int(input()))
res=0
total=sum(dogs)
def dfs(depth, sumw, pathw):
    global res
    if depth==n:
        if res<sumw and sumw<=c:
            res=sumw
        return
    if sumw>c:
        return
    if total-pathw+sumw<res:
        return
    #넣고
    dfs(depth+1, sumw+dogs[depth], pathw+dogs[depth])
    #안 넣고
    dfs(depth+1, sumw, pathw+dogs[depth])
dfs(0,0,0)
print(res)
