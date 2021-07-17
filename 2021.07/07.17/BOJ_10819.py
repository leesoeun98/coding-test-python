n = int(input())
num=list(map(int, input().split()))
res=[0]*n
visited=[0]*n
answer=[]
def dfs(depth):
    if depth==n:
        ans=0
        for i in range(1, n):
            ans+=abs(res[i]-res[i-1])
        answer.append(ans)
        return
    for i in range(n):
        if visited[i]==0:
            res[depth]=num[i]
            visited[i]=1
            dfs(depth+1)
            visited[i]=0

dfs(0)
print(max(answer))