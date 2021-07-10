n, k = map(int, input().split())
num=list(map(int, input().split()))
m = int(input())
res=[0]*k
cnt=0
def dfs(depth, start):
    global cnt
    if depth==k:
        if sum(res)%m==0:
            cnt+=1
        return
    else:
        for i in range(start, n):
            res[depth]=num[i]
            dfs(depth+1, i+1)
dfs(0, 0)
print(cnt)